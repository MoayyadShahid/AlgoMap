# Jane Street Sample Interview — Part 3: O(1) LRU Memoization
# Source: https://blog.janestreet.com/what-a-jane-street-dev-interview-is-like/
#
# INTERVIEW PROMPT
# -----------------
# FIFO can be bad: a key used constantly can still get evicted just because
# it was inserted early. Switch to LRU (Least Recently Used):
#   - on HIT: mark key as most recently used
#   - on MISS when full: evict the LEAST recently used key
# Still want O(1) get / put / evict.
#
# COMPLEXITY LADDER (say this out loud in the interview)
# ------------------------------------------------------
# 1. timestamps in the dict + linear scan for min → O(n) eviction
# 2. min-heap of (timestamp, key)                  → O(log n) eviction
# 3. hash table + doubly linked list               → O(1) everything  ← target
#
# O(1) LRU DESIGN
# ---------------
# Hash table: key -> node
# Doubly linked list of nodes, with sentinel head/tail:
#   - MOST recently used  = next to head (front)
#   - LEAST recently used = prev of tail (back)
#
# On HIT:  splice node out of its current spot, move to front. O(1)
# On MISS: if at capacity, remove node at back + delete from map; then
#          create node, insert at front, add to map. O(1)
#
# WHY DLL + HASH?
# - hash gives O(1) find-by-key
# - DLL gives O(1) remove-from-middle AND O(1) pop-LRU (need prev+next)
# - a singly linked list is NOT enough: removing an arbitrary node is O(n)
#   unless you also store prev pointers (i.e. you reinvent a DLL)
#
# Python note: collections.OrderedDict / functools.lru_cache do this for you.
# In the interview, BUILD the DLL — they want the data-structure insight.
# (LeetCode 146 "LRU Cache" is the same core idea.)
#
# BAR: strong candidates finish Part 3; not finishing ≠ auto-reject.
#      Discussion of the complexity ladder matters as much as code.

from typing import Callable, Dict, Optional


class _Node:
    # doubly linked list node holding one cached (key, value)
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev: Optional["_Node"] = None
        self.next: Optional["_Node"] = None


class LRUMemo:
    def __init__(self, f: Callable[[int], int], capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.f = f
        self.capacity = capacity
        self.map: Dict[int, _Node] = {}

        # sentinels so we never special-case empty / single-node edges
        # head <-> ...nodes... <-> tail
        self.head = _Node()  # MRU side
        self.tail = _Node()  # LRU side
        self.head.next = self.tail
        self.tail.prev = self.head

    # ----- DLL helpers (all O(1)) ----------------------------------------
    def _add_to_front(self, node: _Node) -> None:
        # insert node right after head (= most recently used)
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node  # type: ignore[union-attr]
        self.head.next = node

    def _remove(self, node: _Node) -> None:
        # splice node out: prev <-> next
        node.prev.next = node.next  # type: ignore[union-attr]
        node.next.prev = node.prev  # type: ignore[union-attr]
        node.prev = node.next = None

    def _move_to_front(self, node: _Node) -> None:
        self._remove(node)
        self._add_to_front(node)

    def _evict_lru(self) -> None:
        # node just before tail is least recently used
        lru = self.tail.prev
        assert lru is not None and lru is not self.head
        self._remove(lru)
        del self.map[lru.key]

    # ----- public API ----------------------------------------------------
    def __call__(self, x: int) -> int:
        # HIT: refresh recency, return cached value
        if x in self.map:
            node = self.map[x]
            self._move_to_front(node)
            return node.value

        # MISS: evict if full, then compute + insert as MRU
        if len(self.map) >= self.capacity:
            self._evict_lru()

        value = self.f(x)
        node = _Node(x, value)
        self._add_to_front(node)
        self.map[x] = node
        return value


def memo_lru(f: Callable[[int], int], capacity: int) -> Callable[[int], int]:
    return LRUMemo(f, capacity)


# --- teach-yourself demo -------------------------------------------------
calls = []


def expensive(n: int) -> int:
    calls.append(n)
    print(f"  computing f({n})...")
    return n * 10


if __name__ == "__main__":
    g = memo_lru(expensive, capacity=2)

    # insert 1, then 2 → MRU→LRU order: 2, 1
    assert g(1) == 10
    assert g(2) == 20

    # HIT on 1 → move 1 to front → order: 1, 2
    calls.clear()
    assert g(1) == 10
    assert calls == [], "hit must not recompute"

    # MISS on 3 → evict LRU (2) → order: 3, 1
    # contrast with FIFO: FIFO would have evicted 1 (oldest insert)
    assert g(3) == 30

    calls.clear()
    assert g(2) == 20
    assert calls == [2], "2 should have been LRU-evicted"

    # before that miss, order was 3,1 — so 1 was evicted when 2 arrived
    # current order: 2, 3
    calls.clear()
    assert g(3) == 30
    assert calls == [], "3 is still MRU's neighbor / still cached"

    calls.clear()
    assert g(1) == 10
    assert calls == [1], "1 was evicted earlier when 2 was re-inserted"

    print("Part 3 OK")

# Run Time: O(1) average per call
# Space:    O(capacity)
