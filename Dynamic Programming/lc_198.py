class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # base case: if size of nums is 1, then return the first element
        if n == 1:
            return nums[0]
        # we are going to do Bottom Up Tabulation, where we basically are going to have a running sum
        vals = [0] * n
        vals[0] = nums[0]
        vals[1] = max(nums[0], nums[1])

        for i in range(2, n):
            vals[i] = max(nums[i] + vals[i - 2], vals[i - 1])
        
        return vals[-1]
    # Run Time: O(N)