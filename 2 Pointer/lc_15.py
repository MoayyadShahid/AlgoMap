class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        '''
        So the idea here is that we have 3 ptrs. So much for 2 ptr problem. Anyways, the goal here is to go through each
        element/index and then for each one of those elements we have a left and right ptr (2 ptr) problem where we try to 
        find a combination of 3 numbers that sum to 0. The goal is we get a ptr i, which serves as the '3rd' ptr that goes
        through the entire array, and then we have left and right ptr which serve to find the 2 other values that MAY 
        sum up with the 'i' ptr to equal 0. 

        We first begin with sorting the array.
        '''

        # Sort the array first to make it easier
        nums.sort() # O(N log N)
        result = [] # this will be the array that will store the triples

        # We loop through the entire array
        for i in range(len(nums)): # O(N)
            # If we reach a point where the number that is our 'pivot' or 'i' ptr is positive, then we can't get a sum of 0
            # as there won't be a negative number ahead of the 'i' ptr since we sorted the numbers before hand
            if nums[i] > 0:
                break # break out of the outer loop, leading to us returning the array
            # this is to see if we are getting repeat negative numbers, if we find one, then we just skip that case
            # as we already handled it initially
            elif i > 0 and nums[i] == nums[i - 1]: 
                continue
            
            # define the left and right ptrs, which will be in the sub-array of the list, which is the list beyond the 'i' ptr
            left = i + 1
            right = len(nums) - 1
            # now we are going through the 'sub-array' until left and right ptr crossover
            while left < right: # O(N)
                # we define the sum of the triple and go through 3 cases
                summ = nums[i] + nums[left] + nums[right]
                # case 1: the sum equates to 0
                if summ == 0:
                    # add the triple
                    result.append([nums[i], nums[left], nums[right]])
                    # increment the left ptr
                    left += 1
                    # decrement the right ptr
                    right -= 1
                    # after altering the ptrs, we want to see if we are on a repeated number, if so we alter the ptrs further
                    # if the left ptr after being increment above is the same number as we just handled, then we increment till we don't repeat the same number
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # if the right ptr after being decrement above is the same number as we just handled, then we decrement till we don't repeat the same number
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                # otherwise if we have the sum being less than 0, then we increment the left ptr to get a greater left ptr number
                elif summ < 0:
                    left += 1
                # else if we have the sum being greater than 0, then we decrement the right ptr to get a lesser right ptr number
                else:
                    right -= 1 
        # return the triples
        return result
        # Run Time: O(N^2)
        