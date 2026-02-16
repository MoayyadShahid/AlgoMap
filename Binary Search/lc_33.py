class Solution:

    def search(self, nums: List[int], target: int) -> int:
        # we will first find the partition by finding the smallest element and split the array into 2 halfs
        low = 0
        high = len(nums) - 1
        mini = 0

        while low < high:
            mid = (low + high) // 2
            
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        
        # set the index of the minimum value
        mini = low

        # after determining the index of the minimum value, we will now partition the array and then run binary search
        # to find the target value

        # there is an edge case that the array is already in increasing order, in which case the minimum value is at index 0
        # or the start
        if mini == 0:
            l, r = 0, len(nums) - 1
         
        # if the target value is in the lower half partition, set the left and right variables for the binary search
        elif nums[0] <= target <= nums[mini - 1]:
            l, r = 0, mini - 1
            
        # else the target value is in the upper half partition
        else:
            l, r = mini, len(nums) - 1
        
        # apply the binary search in the respective partition with the given l and r indices
        while l <= r:
            mid = (l + r) // 2            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        # if value not found, return -1 or the error value
        return -1
    # Run Time: O(log N)
