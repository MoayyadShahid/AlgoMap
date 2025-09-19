class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        The idea here is as follows, we have 2 ptrs and those represents the heights, we essentially
        just do a usual 2 ptr algorithm where we move the lower height ptr towards the center. Further
        as we go through the heights list we basically compare which one of the heights is smaller and increment
        that one towards the center with the goal that we may find a larger height. 
        '''
        # define the ptrs
        left = 0
        right = len(height) - 1
        # define the max area
        maxArea = 0
        # loop through the height list till we crossover the ptrs
        while left < right:
            # the base of the area is the distance between right ptr and left ptr
            base = right - left
            # the current area is the base * the minimum of the heights as that is the most the water can go up to
            currArea = min(height[left], height[right]) * base
            # then we check if we got a greater value for the area
            if currArea > maxArea:
                maxArea = currArea
            # if left ptr height is smaller than right ptr height, then increment left ptr
            if height[left] < height[right]:
                left += 1
            # else right ptr height is smaller than left ptr height, so decrement right ptr
            else:
                right -= 1
        # return max area
        return maxArea
        # Run Time: O(N)
