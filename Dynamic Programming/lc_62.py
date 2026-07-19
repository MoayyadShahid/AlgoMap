class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # we're gonna apply bottom up tabulation, just going to have a summation of values from the upper and left cell
        # to get total pathways
        if m == 1 and n == 1 or m == 1 and n > 1 or m > 1 and n == 1:
            return 1
        
        # intialize the pathway tabulation array
        path = [[0 for _ in range(n)] for _ in range(m)]
        path[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                # if we're on the top row, initialize it to all 1's
                if i == 0:
                    path[i][j] += path[i][j - 1]
                # likewise if we're on the first column, initialize it to all 1's
                elif j == 0:
                    path[i][j] += path[i - 1][j]
                # else, we add the values from the top and left cells to get the # of pathways to the current cell
                else:
                    path[i][j] = path[i - 1][j] + path[i][j - 1]
        
        # return the value of pathways to the bottom right cell
        return path[m - 1][n - 1]
    
    # Run Time: O(M * N)
     