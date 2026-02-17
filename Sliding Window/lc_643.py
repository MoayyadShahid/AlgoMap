class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # for the sliding window strategy the technique is to first do some operation on a pre-defined window
        # and then loop through the remainder of the possible items in the array/list one at a time, by updating
        # the window with the new value and discarding the element at the start (or at the end, left side) until
        # the entire array has been exhausted with valid window sizes of contiguous blocks
        n = len(nums)
        curr_sum = 0

        # we find the sum of the first window of k elements
        for i in range(k):
            curr_sum += nums[i]
        
        # we define the current maximum average based off the first window of k elements
        max_avg = curr_sum / k

        # then we loop through from the k-th element, to the end, and we will basically determine the average of the
        # 'sliding' window by adding a new element and removing the 'oldest' element at the end
        # then we will get the average of the current window and do a trivial comparison with the current max average
        for i in range(k, n):
            curr_sum = curr_sum + nums[i]
            curr_sum = curr_sum - nums[i - k]
            curr_avg = curr_sum / k

            if curr_avg > max_avg:
                max_avg = curr_avg
        
        # return the maximum average of a k-sized window of contiguous elements
        return max_avg
    # Run Time: O(N)
        