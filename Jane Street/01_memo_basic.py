# Jane Street Sample Interview — Part 1: Basic Memoization
# Source: https://blog.janestreet.com/what-a-jane-street-dev-interview-is-like/
#
# INTERVIEW PROMPT
# -----------------
# Memoization = cache results of a pure function so you never recompute
# the same input twice. Given expensive f: int -> int (output depends only
# on input), return g of the same type where g(x) == f(x) for all x, but
# f is only called once per distinct x.
#
# WHAT THEY WANT TO HEAR
# ----------------------
# - "Pure" / referential transparency: same input always same output, so
#   caching is safe.
# - Data structure: hash table (dict). Average O(1) lookup + insert.
# - Closure: the cache lives outside the returned function but is private
#   to that memoized instance (one cache per call to memo()).
# - Be ready to explain how your language's hash table works and its
#   amortized complexity (Python dict: open addressing, amortized O(1)).
#
# BAR: every successful candidate finishes a bug-free Part 1 quickly.

from typing import Callable, Dict


def memo(f: Callable[[int], int]) -> Callable[[int], int]:
    # the cache is created ONCE when memo(f) is called, then captured by
    # the inner function. every call to g shares this same dict.
    results: Dict[int, int] = {}

    def g(x: int) -> int:
        # hit: return the stored answer, never touch f again for this x
        if x in results:
            return results[x]

        # miss: pay the expensive cost once, then remember it forever
        value = f(x)
        results[x] = value
        return value

    return g


# --- teach-yourself demo -------------------------------------------------
# pretend f is expensive: each call prints so you can SEE when it runs
def expensive_square(n: int) -> int:
    print(f"  computing f({n})...")
    return n * n


if __name__ == "__main__":
    g = memo(expensive_square)

    print("g(3) first time:")
    assert g(3) == 9          # should print "computing..."

    print("g(3) second time:")
    assert g(3) == 9          # should NOT print — cache hit

    print("g(4) first time:")
    assert g(4) == 16         # miss → compute

    print("g(4) again:")
    assert g(4) == 16         # hit

    print("Part 1 OK")

# Run Time: O(1) average per call after the first computation for that key
# Space:    O(U) where U = number of unique inputs ever seen  ← THIS is Part 2's problem
