import heapq as hp

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # we modify the values in the nums list so we invert their values to be stored in the correct order of the heap
        for i in range(len(nums)):
            nums[i] = -nums[i]
        
        # turn the nums list into a heap using heapify
        hp.heapify(nums)

        # we remove the first k - 1 largest numbers
        for i in range(k - 1):
            hp.heappop(nums)
        
        # after popping off the first k - 1 largest numbers we will have the k'th largest number
        return -nums[0]
    # Run Time: O(N)