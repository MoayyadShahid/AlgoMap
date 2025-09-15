class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        '''
        Okay this is a classic 2 pointer problem. The idea is that we basically swap every outer element
        with each other as we move the pointers sequentially to the center element, resulting in a reversed string.
        '''
        # create the left and right ptrs
        left = 0
        right = len(s) - 1
        # we will loop through 's' and continue until we crossover the left and right ptrs
        while left <= right: # O(N)
            # just a classic variable swap
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            # increment the left and decrement the right ptrs
            left += 1
            right -= 1
        # Run Time: O(N)
