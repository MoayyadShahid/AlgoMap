class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create empty the list of 2 index
        rng = []
        # go through each element index
        for m in range(len(nums)):
            # loop over every element index above the current one (m)
            for n in range(m + 1, len(nums)):
                # check it the sum of the current m and n equate to target
                if nums[m] + nums[n] == target:
                    rng = [m, n]
        return rng
        # Run Time: O(N^2)
        