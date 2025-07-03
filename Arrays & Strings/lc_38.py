class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # Transpose
        for i in range(0, n):
            for j in range(i+1, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        # Horizontal Flip
        if n % 2 == 0:
            for i in range(0, n):
                for j in range(0, n // 2):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[i][n - j - 1]
                    matrix[i][n - j - 1] = temp
        else:
            for i in range(0, n):
                for j in range(0, n // 2):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[i][n - j - 1]
                    matrix[i][n - j - 1] = temp
            


        