# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        isBad = n

        while low <= high:
            mid = (low + high) // 2

            if isBadVersion(mid) == False:
                low = mid + 1
            else:
                isBad = mid
                high = mid - 1
                
        return isBad

