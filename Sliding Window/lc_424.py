class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # initialize up left ptr
        l = 0
        # we need a way to track all the characters, so the value at index i will be the count of the i-th letter 
        # (where the indexing of the capital letters starts at 0)
        counts = [0] * 26
        # initialize the longest window
        maxW = 0

        # setup the right ptr
        for r in range(len(s)):
            
            # as we go through each letter in the string 's' we will add + track the count of that character in counts list
            # ord(LETTER_IN_S) - ord('A') just gives the index value where to insert the letter in the correct ordering in counts list
            counts[ord(s[r]) - ord('A')] += 1
            # then what we do is we check that the current window that we have for s[l...r] is it the case that the letters
            # we have seen so far is in the case that the window size (r - l + 1) substract the most common letter max(counts)
            # if the remainder of that difference has more separate characters than swappable character limit given by k
            # then we need to tighten the window from the left side, by reducing the count of letters we encounter from the left ptr side
            # and then increment the left ptr
            while (r - l + 1) - max(counts) > k:
                counts[ord(s[l]) - ord('A')] -= 1
                l += 1

            # in the case that we don't need to tighten the window, or in the case that we just did, we now calculate the max width maxW
            maxW = max(r - l + 1, maxW)
        
        # return max width maxW
        return maxW
    # Run Time: O(N)
