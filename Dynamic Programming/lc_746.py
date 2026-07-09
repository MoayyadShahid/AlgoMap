class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # we're gonna approach this problem via BU Tabulation (we could also approach this via sliding window 2 variables, but goal is to practice tabuluation)
        # at each step i / index i we'll have the cost of the minimum cost (where cost is the cost of the step i itself and in the minimum pathway before)
        n = len(cost)
        tab = [0] * n
        tab[0], tab[1] = cost[0], cost[1]

        for i in range(2, n):
            # either at the current step i, we can reach it by going 1 step from the previous step or coming from the 2nd previous step (choose whichever has lowest cost)
            tab[i] = min(cost[i] + tab[i - 1], cost[i] + tab[i - 2])
        
        # at the very end we can reach the top of the stairs either via 1 step or 2 steps, so compare the final 2 steps costs'
        return min(tab[n - 1], tab[n - 2])
    
    # Run Time: O(N)