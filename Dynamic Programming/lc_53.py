class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # we're gonna do something called Kadane's Algorithm, basically keep a running sum, but if at any point 
        # it drops below 0, then restart the running sum
        # keep track of max sum when at any time the current sum exceeds max sum
        if len(nums) == 1:
            return nums[0]

        summ = 0
        maxx = nums[0]

        for i in range(len(nums)):
            summ += nums[i]

            if summ > maxx:
                maxx = summ
            if summ < 0:
                summ = 0

        return maxx
    # Run Time: O(N)
