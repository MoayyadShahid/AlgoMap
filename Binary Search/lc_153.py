class Solution:
    def findMin(self, nums: List[int]) -> int:
        # set up binary search low and high variables
        low = 0
        high = len(nums) - 1

        # not inclusive as we don't want to crossover, we want to equate/converge at a minimum value point
        while low < high:
            # calculate the mid
            mid = (low + high) // 2

            # if the mid point value is greater then we increase the lower range and focus on the upper half
            if nums[mid] > nums[high]:
                low = mid + 1
            # otherwise if the mid value is smaller than the high value, then we reduce to focus on the lower half
            else:
                high = mid

        # since we have a loop of '<' then we will have low == high after the loop is done
        return nums[low]
    
    # Run Time: O(log N)
