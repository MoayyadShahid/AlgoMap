class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # this is going to be a fixed sliding window problem
        # we define the lengths that we need
        n1 = len(s1)
        n2 = len(s2)

        # we are going to track the character frequencies by having count1 track s1
        # and count2 track s2 in a window format of the size of s1, so we can see at any time
        # of the window if count1 == count2 where the window equates the frequency meaning that a permutation is possible
        count1 = [0] * 26
        count2 = [0] * 26

        # if s1 is bigger than s2, no permutation is possible, quick False
        if n1 > n2:
            return False

        # we first set the frequencies of s1, and also s2, but for s2 we go upto the size of s1
        for i in range(n1):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        
        # if the first n1 characters are a permutation then we return True, otherwise we continue
        if count1 == count2:
            return True
        
        # now we having a sliding window, where we add a character and remove a character each iteration
        # the window size is [i - n1] or from i - n1 to i, essentially i - (i - n1) = n1 size window
        for i in range(n1, n2):
            # add new element to n1 sized window
            count2[ord(s2[i]) - ord('a')] += 1
            # remove oldlest element from n1 sized window
            count2[ord(s2[i - n1]) - ord('a')] -= 1

            # if after doing the frequency update after shifting the window we have equal frequencies then return True
            # for a permutation existing
            if count1 == count2:
                return True

        # if after the entire loop, we have no permutation existing return False
        return False
    # Run Time: O(N)
