class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

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
     