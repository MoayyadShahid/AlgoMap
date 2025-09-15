class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
        Brute force solution. First create an array that is the squared version of nums.
        Then use the built-in sort method to sort the array in non-decreasing order.
        '''
        sqrd = [x*x for x in nums] # O(N)
        sqrd.sort() # O(N log N)
        return sqrd 
        # Run Time: O(N log N)
        