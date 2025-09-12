from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        So the strategy here is as follows:
        We create a default_dict which has empty default value of a list [], and the idea is
        that we go through each string in the list strs, and we create a list encoding of
        the frequency of each of the 26 possible charaters in the string str in the list of strs
        then from there we turn that encoded list into a tuple since tuple's are immutable and ordered
        allowing them to serve as keys for dictionaries. Next we simply use that tuple / frequency encoded list
        to serve as the key and have the current string str we are checking in the strs list to be added as a value
        for that current tuple. In the end we just return the values of all the keys, which is the answer we're looking for.
        '''
        
        anagrams_dict = default_dict(list) # create default dictionary with empty list
        # loop through all strings in strs 
        for s in strs: # O(N)
            count = [0] * 26 # create the encoding list for the frequency of each character of the current string
            for c in s: # O(M) 
                count[ord(c) - ord('a')] += 1 # ord(...) function returns the ASCII value of a char in python
            
            # turn the list into a tuple
            key = tuple(count) # O(M)
            anagrams_dict[key].append(s) # add the current string to the tuple / frequency encoded list
        
        # return all the grouped anagrams in a list
        return anagrams_dict.values()
        # Run Time: O(N * M)
        