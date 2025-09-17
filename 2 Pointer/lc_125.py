class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        Another classic 2 pointer problem. What we will do is first turn the string into a list of valid
        alphanumeric characters that are all lower case. Then we will define left and right 'ptrs' that
        will go from the ends of the array and check if the elements match up. If not return False, else return True.
        '''
        lst = [] 
        # loop through the string and add only alpha-numeric elements to the list
        for i in s: # O(N)
            if i.isalnum():
                lst.append(i.lower())
        # create the 'ptrs'
        left = 0
        right = len(lst) - 1
        # go through the list till the 'ptrs' crossover each other
        while left <= right:
            if lst[left] != lst[right]: # if characters don't match when they should, then it's not a palindrome
                return False
            # update the positions of the 'ptrs'
            left += 1
            right -= 1
        # otherwise we have gone through the list and everything matches up
        return True
        # Run Time: O(N)
