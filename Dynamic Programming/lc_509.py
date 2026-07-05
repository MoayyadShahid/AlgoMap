class Solution:
    def fib(self, n: int) -> int:
        # track the previous and current
        prev = 0
        curr = 1

        # guardian checks, if n == 0 or n == 1 return their respective values
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            # otherwise, we will loop from 2 to N (inclusive) and then set curr to the next Fibonnaci number (curr + prev) and prev to curr
            for _ in range(2, n + 1):
                curr, prev = prev + curr, curr
            # at the very end we just want curr value 
            return curr
        
        # Run Time: O(N) 
