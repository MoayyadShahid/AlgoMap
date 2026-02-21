class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # set the left ptr
        l = 0
        # since we want a minimum window we set the window tracker to max value, or we can also do float('inf')
        minW = 10**9 # could also set it to float('inf')
        sum = 0

        # we will set the right ptr
        for r in range(len(nums)):
            # we want the minimum window size that satisfies the target >= of the target
            # track the sum so far
            sum += nums[r]
            
            # if the sum in our current window between l ptr and r ptr is greater than target then we need 
            # determine if its a minimum window size or not
            while sum >= target:
                # check if we found a smaller window size
                minW = min(minW, r - l + 1)
                # we need to update the sum by reducing number elements we encountered from the left
                sum -= nums[l]
                # increment the left ptr
                l += 1
        
        # now over here we are checking the condition that if the left ptr didn't move at all and we exhausted the list
        # then we have the scenario that the sum of the ENTIRE list is smaller than the target, so we return 0 as no sub-array works
        if l == 0 and sum < target:
            return 0

        # another way of checking instead of the above final conditional is by doing
        #return minW if minW < 10**9 else 0
        return minW
        # Run Time: O(N)
