# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # We're going to do a standard binary search algorithm. 
        # This time, we're going to set the low as the first element and the high as the nth element. 
        low = 1
        high = n
        # We're going to assume that isBad is set to the last element or nth element.
        # The reason we do this is because we are basically going to move that pointer of the isBadElement towards left. 
        isBad = n

        # This is the standard condition, while condition for binary search. 
        while low <= high:
            # Set the midpoint. 
            mid = (low + high) // 2

            # We want to update the low pointer to point up into the upper half. 
            if isBadVersion(mid) == False:
                low = mid + 1
            # Otherwise, we've got the bad version, and so we reduce the high pointer to the lower half, 
            # but we FIRST indicate that the latest iteration of isBad is equivalent to the mid pointer. 
            else:
                isBad = mid
                high = mid - 1
                
        # Once we're done, we return the i-th element which is isBad. 
        return isBad
    
    # Run time is O(log n). 

