class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # the idea here is basically the same as lc_200, where we just have an accumulator for each island we dfs on
        m, n = len(grid), len(grid[0])
        curr_area, max_area = 0, 0

        # we have a base case of returning 0 when we get out of the island bounding
        # else we do 1 + recursive call on DFS in 4 directions (up, down, left, right)
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return 0
            grid[i][j] = 0
            return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)      
        
        # we loop through the grid to find valid starting points to do DFS by finding starting spots of 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # we get the area of the current island
                    curr_area = dfs(i, j)
                    # if the current island is greater than the largest island we found, we update max_area
                    if curr_area > max_area:
                        max_area = curr_area

        return max_area
    # Run Time: O(M * N)
