class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       # set row and col values
       row = len(matrix)
       col = len(matrix[0])
       
       # set binary search low and high
       low = 0
       high = row*col - 1
       
       # start binary search
       while low <= high:
           # define mid value index
           mid = (low + high) // 2
           # linearize 2D Matrix by getting values of row and col mid index
           row_m = mid // col
           col_m = mid % col
           # get the value of the mid index
           val = matrix[row_m][col_m]

           if val == target:
               # value found
               return True
           # search lower half
           elif val > target:
               high = mid - 1
           # search upper half
           else:
               low = mid + 1

       # value not found
       return False
    
    # Run Time: O(log N) 
        