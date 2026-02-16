class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we have a speed of eating/hour of k, and we have this nested function to determine if the speed/rate
        # is fast enough to eat all the bananas in the piles in each pile (or at least some from each pile but touching all piles)
        def k_works(k):
            hours = 0
            # we go through each pile
            for pile in piles:
                # we add the time it takes to each all the bananas in each pile given the rate k bananas/hour
                hours += ceil(pile / k)
            # if we can eat all the bananas at the rate k within h hours then we return True that this rate k works
            return hours <= h
        
        # we are gonna set the lower and upper variables for binary search as the values of k, which can be either
        # 1 banana/hour or max(piles) or the max value of bananas in all of the piles per hour
        # we want to converge and find the smallest one that can get the job done
        l = 1
        r = max(piles)

        # we want to converge on a specific k value so we will have '<'
        while l < r:
            # go to the mid-point of the potential values of k
            k = (l+r) // 2
            # check if that value of k is feasible, not if it is the minimum yet
            # if it is feasible we focus on the lower half of the interval
            if k_works(k):
                r = k
            # if the mid value isn't feasible k value, we focus on the upper half of the interval
            else:
                l = k + 1
        
        # since we had '<' in the loop condition, then at the end we have l = r, or we have converged on the value
        # which is the minimum k value that can get the job done
        return l
        # Run Time: O(N * log(max(piles))) OR O(N * log(M))
        