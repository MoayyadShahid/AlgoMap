class Solution:
    '''
    This is a classic binary search algorithm implemenation
    '''
    def search(self, nums: List[int], target: int) -> int:
        # we create a low and high, classic 2 ptr technique
        low = 0
        high = len(nums) - 1

        # we loop through the array, until we get a crossover of low and high, where low > high
        while low <= high:
            # we calculate the mid point
            mid = (low + high) // 2

            # we check if the num at mid is equal, then return the mid index
            if nums[mid] == target:
                return mid
            # otherwise if mid index num is greater than target, we adjust the high index to be lower
            elif nums[mid] > target:
                high = mid - 1
            # else if the mid index num is lesser than target, we adjust the lwo index to be higher
            else:
                low = mid + 1
        
        # if we didn't return a valid index, we return -1 to indicate failure to find
        return -1
    # Run Time: O(log N)
