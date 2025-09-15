class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
        the idea with this implementation is that we will use the squared array, and then go from
        the ends of the squared array and add values to a new ordered array based on comparison.
        the pattern we identified is that since the nums list is non-decreasing, then when we make the squared
        array from that base 'nums' list, we will essentially have it that the largest elements are suppose to be
        on the outer ends of the array while the smallest element is in the center. So that is why we apply the
        2 pointer technique / squeeze technique, where we setup the 'pointers' to start off at the opposite ends of
        the array and the sequentially go through till be crossover or reach 'left <= right' scenario.
        '''
        # First get an array of all the squared elements in 'nums'
        sqrd = [x*x for x in nums] # O(N)
        final = []
        # set up the pointers
        l = 0
        r = len(sqrd) - 1
        # we will loop through the squared array 'sqrd' till we have an overlap between left_ptr and right_ptr
        while l <= r:
            # we set up variables to easily access the values of the elements that the right and left pointers are indicating
            r_val = sqrd[r]
            l_val = sqrd[l]
            # we first check if right ptr element is greater than left ptr element
            if  l_val < r_val:
                # if so, add the right element to the ordered array
                final.append(r_val)
                r -= 1 # decrement the position of the right ptr
            # otherwise, we have it that the left ptr element is greater than right ptr element
            else:
                # add left ptr element to ordered array
                final.append(l_val)
                l += 1 # increment the position of the left ptr
        final = final[::-1] # since we were adding greatest -> least elements, we need to reverse the ordered array to get least -> greatest
        return final
        # Run Time: O(N)
