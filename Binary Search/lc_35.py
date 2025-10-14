class Solution:
    '''
    this is a slight modification of the classic binary search algorithm. We will check 5 things when
    we will calculate the mid and use it in the following way:

    1. if the target is equal to the num at mid index we return mid index 
    2. otherwise if the target is greater than the highest element we return highest index + 1
    3. otherwise if the target is smaller than the lowest element we return lowest index (since lowest would become lowest + 1)
    4. otherwise if the target is smaller than the mid index then we update the high index to be smaller
    5. otherwise if the arget is greater than the mid index then we update the low index to be higher
    '''
    def searchInsert(self, nums: List[int], target: int) -> int:
        # set the 2 ptrs for low and high index
        low = 0
        high = len(nums) - 1

        # loop through the array until we have a crossover of low and high index where low > high
        while low <= high:
            # we calculate the mid index
            mid = (low + high) // 2

            # go through the conditions we outlined above
            if target == nums[mid]:
                return mid
            elif target > nums[high]:
                return high + 1
            elif target < nums[low]:
                return low
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1            
     
    # Run Time: O(log N)