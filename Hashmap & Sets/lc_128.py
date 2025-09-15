class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        okay the idea here is to use the hashing concept of sets as they have O(1) lookup.
        What we essentially do is convert the nums list into a set, so any repeated elements are ignored.
        Then we loop through the nums and essentially see if it is the lowest occuring element in a sequence.
        From that lowerst occuring number what we do is see how long the consecutive chain that lowest number forms.
        '''
        # turn nums into a set
        s = set(nums) # O(N)
        longest = 0 
        # go through the set version of nums
        for num in s:
            if num - 1 not in s: # we want to only consider numbers that are the smallest in their sequence
                next_num = num + 1 # we define the next possible number in the sequence
                length = 1 # set the temporary length of the current explored sequence
                while next_num in s: # loop through the seqeuence of possible next numbers as long as they exist in the set
                    length += 1 # increase the temporary length
                    next_num += 1 # update the next number in the sequence to be checked
                longest = max(longest, length) # after each exploration of the current smallest sequence number, we compare it with
                # higher scoped length stored (longest) to see what is the longest length we've explored so far
        return longest 
        # Run Time: O(N)
