class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # This is a variable sliding window problem
        # set left pointer
        l = 0
        zeroes = 0
        # set variable to track the max gap
        maxW = 0

        # set the right pointer, which will be variable as it goes through the entire array
        # when there is a condition that affects the tracking the left pointer will update accordingly
        for r in range(len(nums)):

            # if we encounter a 0 while incrementing the right pointer, then we increment the condition of zeroes
            if nums[r] == 0:
                zeroes += 1
            
            # as we are incrementing the right pointer we will see the valid consecutive groups of 1's 
            # if we notice that we've exhausted our total conversion capability of k-vals, then we have to move
            # the left pointer and see if we can gain back our k # of switchable binary values
            while zeroes > k:
                # if we encounter the condition, we reduce the zeroes we encountered for our k # of switchable values
                if nums[l] == 0:
                    zeroes -= 1
                # keep incrementing the left pointer
                l += 1
            
            # the max width is either the current standing between right ptr (r) and left ptr (l) which is r - l + 1, 
            # or it could be the already previously found max width maxW
            maxW = max(r - l + 1, maxW)
        
        # return the max width maxW
        return maxW
    # Run Time: O(N)
