class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # since we are trying to determine the longest UNIQUE continguous substring
        # we need to keep track of what we've seen so we don't have repeats
        # use a set to keep track
        seen = set()
        # setup the left ptr
        l = 0
        # setup the max window seen
        maxW = 0

        # setup the right ptr
        for r in range(len(s)):

            # now if we have a scenario where the ptr lands on a character we've already seen we need 
            # to basically keep removing elements from the left from seen / move the left ptr 
            # so that we reach a state where we know that we don't have any repeating characters when
            # we work with to create a new continuous UNIQUE substring with the character s[r] or where the right ptr is located
            while s[r] in seen:
                # first remove the element from the set at the left ptr
                seen.discard(s[l])
                # update the left ptr
                l += 1
                # basically when we remove the char in seen set that left ptr points to we either say that the left to right ptr
                # substring either starts with a char that is equal to s[r] or it either has a char in between left ptr and right ptr
                # that is equal to s[r] so we have to keep moving the left ptr till we pass that repeating element to begin a 
                # unique contiguous substring
        
            # in the case that s[r] hasn't been added to the set 'seen' or if it was removed by the loop above
            # then we re-add/add it
            seen.add(s[r])
            # we determine the max width based on the position of the left and right ptrs or if there was already a previous found max width
            maxW = max(r - l + 1, maxW)
            
        # return max width
        return maxW
        # Run Time: O(N * M) ~ O(N)
    