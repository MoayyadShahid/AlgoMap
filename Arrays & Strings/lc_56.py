class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # first we will sort the intervals list by each inner list's
        # first element, so we have interval blocks with the starting num
        # in order
        intervals.sort(key = lambda interval: interval[0])

        # this is going to be our merged intervals array
        M = []
        # we go through each interval block and will see how it fits in M
        for i in intervals:
            # if M is empty, then add the initial interval
            # Or, if the most recently added block in M has its ending interval
            # num less than the block we are currently on (i) then we can
            # add the new block
            # basically we are seeing if the new block (i) should simply be added
            # by checking if M is empty or if (i) doesn't overlap with the latest
            # block in M
            if M == [] or M[-1][1] < i[0]:
                M.append(i)
            # otherwise, we have an overlap between (i) and the latest block in M
            # what we will do is modify the latest block in M, by taking the
            # the starting element in M, since after the sorting it clearly should
            # be smaller than i, and we will take the ending element as the
            # max between the ending element of (i) or of the latest M
            else:
                M[-1] = [M[-1][0], max(M[-1][1], i[1])]
        
        return M
        
        # Solution Runtime: O(N log N)