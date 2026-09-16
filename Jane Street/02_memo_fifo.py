# Jane Street Sample Interview — Part 2: Bounded FIFO Memoization
# Source: https://blog.janestreet.com/what-a-jane-street-dev-interview-is-like/
#
# INTERVIEW PROMPT
# -----------------
# Part 1's cache grows forever → memory leak under many distinct inputs.
# Fix: bound the cache size and evict in FIFO order when full.
# Goal: O(1) eviction (not a linear scan of the table).
#
# WHAT THEY WANT TO HEAR
# ----------------------
# Problem: unbounded growth / memory leak — memo can make prod WORSE.
# Fix idea: capacity + eviction policy.
#
# FIFO trade-offs vs other policies:
#   + simple, true O(1) with a queue + hash table
#   + fair "oldest insertion leaves first"
#   - ignores RECENT use: a hot key inserted early can get evicted while
#     cold keys inserted later stay. that's why Part 3 moves to LRU.
#
# O(1) FIFO design:
#   - dict: key -> value          (lookup / store)
#   - queue (deque): insertion order of keys
#   - on miss when full: popleft the oldest key, delete from dict, then insert
#
# Gotcha to mention: if the same key is requested again while still cached,
# FIFO does NOT move it — insertion order only. (LRU would refresh it.)
#
# BAR: most candidates they pass finish Part 2 fully.

from collections import deque
from typing import Callable, Deque, Dict


def memo_fifo(f: Callable[[int], int], capacity: int) -> Callable[[int], int]:
    if capacity <= 0:
        raise ValueError("capacity must be positive")

    results: Dict[int, int] = {}
    order: Deque[int] = deque()   # oldest key at the LEFT

    def g(x: int) -> int:
        # cache hit — FIFO does nothing special on hits
        if x in results:
            return results[x]

        # cache miss — maybe evict before inserting
        if len(results) >= capacity:
            oldest = order.popleft()   # O(1)
            del results[oldest]        # O(1) average

        value = f(x)
        results[x] = value
        order.append(x)                # O(1)
        return value

    return g


# --- teach-yourself demo -------------------------------------------------
calls = []


def expensive(n: int) -> int:
    calls.append(n)
    print(f"  computing f({n})...")
    return n * 10


if __name__ == "__main__":
    g = memo_fifo(expensive, capacity=2)

    # fill cache: {1, 2}, oldest = 1
    assert g(1) == 10
    assert g(2) == 20

    # hit on 1 — FIFO does NOT refresh order; oldest is still 1
    calls.clear()
    assert g(1) == 10
    assert calls == []

    # miss on 3 → evict oldest (1), cache becomes {2, 3}
    assert g(3) == 30

    # 1 was evicted, so this recomputes; then oldest (2) is evicted → {3, 1}
    calls.clear()
    assert g(1) == 10
    assert calls == [1], "1 should have been FIFO-evicted and recomputed"

    # 2 was evicted when 1 was re-inserted
    calls.clear()
    assert g(2) == 20
    assert calls == [2]

    print("Part 2 OK")

# Run Time: O(1) average per call (dict + deque ops)
# Space:    O(capacity) — bounded, unlike Part 1
