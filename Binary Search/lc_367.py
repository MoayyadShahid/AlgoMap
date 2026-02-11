class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # initialize binary search low + high vars
        low = 1
        high = num

        # create loop condition
        while low <= high:
            mid = (low + high) // 2

            # we then get the squared value of the mid
            sqr = mid * mid
            # if sqr is == to num, then we have the squareroot
            if sqr == num:
                return True
            # otherwise if sqr is greater than num, then our squareroot mid is bigger
            # we need to focus on lower half
            elif sqr > num:
                high = mid - 1
            # else we have a smaller squareroot so we need to focus on upper half
            else:
                low = mid + 1
        
        # return false if we didn't get anything
        return False
    
    # Run Time: O(log n)
