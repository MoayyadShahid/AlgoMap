class Solution:
    def climbStairs(self, n: int) -> int:
        # the possibilities are actually the N + 1 fibonnaci numbers
        prev = 1
        curr = 1

        if n == 1:
            return curr
        for i in range(2, n + 1):
            prev, curr = curr, prev + curr
        
        return curr
        # Run Time: O(N)