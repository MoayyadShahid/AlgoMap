class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        #The strategy here is that we will first take the Transpose, and then Horizontal Reflection

        # Transpose
        # Go through each row
        for i in range(0, n):
            # We will see each element that starts one more from the diagonal
            # so here we choose column index j, that is 1 more than the current diagonal element
            for j in range(i + 1, n):
                # swap the elements across the diagonal, so ij <-> ji
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        # Horizontal Flip
        # go through each row
        for i in range(0, n):
            # go to the mid-way point of each row
            for j in range(0, n // 2):
                # swap the elements with its corresponding outer-pair
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][n - j - 1]
                matrix[i][n - j - 1] = temp

        # Time Complexity: O(N^2), since we do 2 nested loops of size N


        