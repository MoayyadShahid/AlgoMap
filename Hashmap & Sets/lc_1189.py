class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        '''
        The goal here is we turn the 'text' string into a hashmap / dictionary of letter : occurrences
        specfically of letters that are used to make 'balloon'. Then we use that hashmap and then get 
        the maximum count value by seeing the minimum value of possible construcing letters we can use.
        '''
        bMap = {}
        valid = {'b','a','l','o','n'} # we use a set as the 'in' operation is O(1) time whereas a list as O(N) time for 'in'

        # construct the hashmap but only add the valid letters / letters that make 'balloon' to the hashmap
        for i in text:
            if i in valid: # O(1) operation since valid is a set
                bMap[i] = bMap.get(i, 0) + 1
        
        # first check is to see that keys must be only valid letters, if the keys list isn't == 5 then we can't make a single balloon
        if len(bMap.keys()) != len(valid):
            return 0
        
        # create count, and initialize to a random valid letter since all of them must be in the hashmap
        count = bMap['b']
        for i in bMap.keys(): # go through each letter, and then update count based on the letter we are dealing with
            # see how many max 'balloon' can be constructed by dividing the count by component letters
            # for 'l' and 'o' we floor divide by 2 because we need 2 of each for each 'balloon'
            if i == 'l':
                count = bMap['l'] // 2 if bMap['l'] // 2 < count else count

            elif i == 'o':
                count = bMap['o'] // 2 if bMap['o'] // 2 < count else count
            # for the other valid letters we just compare its occurrences with the count value
            else:
                count = bMap[i] if bMap[i] < count else count
        # return count
        return count
        # Run Time: O(N)
