class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        the idea is that since the Maj element is there more than len / 2 times
        then if we have some sort of polling system where we increment / decrement the counter
        going through the array while maintaining a 'flag' / 'tracker' of the current candidate
        then we would essentially land on having the majority element as that 'flagged' candidate
        '''
        
        # set the candidate count to 0
        count = 0
        candidate = nums[0] # just choose the first element of the array as the candidate Maj element

        # go through the array, starting off index 1
        for i in range(1, len(nums)):
            # first of all, if the current number is the same as the candidate we increase the 'flag' count
            if nums[i] == candidate:
                count += 1
            # otherwise if we have it that the count is 0, we either have 2 situations, first of all
            # the candidate didn't have another element so we need to switch our candidate to the current
            # or the other scenario is that the candidate exhausted its 'flag' count
            # regardless we need to swap the candidate for the current element
            elif count == 0:
                candidate = nums[i]
            # otherwise if the count is positive and the current element isnt the same as the candidate
            # we will decrease the count by 1
            else:
                count -= 1
        # return the majority element which is the candidate
        return candidate
        # Run Time: O(N)
