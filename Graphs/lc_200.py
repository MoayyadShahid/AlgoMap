class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # since we want to determine separate islands, we need to do a DFS
        # the idea here is that we will find valid starting points which are "1" and we will run DFS on the given graph 'grid'
        # by expanding in all possible directions 'up', 'down', 'right', 'left' and we will mark those as '0', and we will keep doing so
        # until we no longer can do so demarcating a maximal island
        m, n = len(grid), len(grid[0])
        islands = 0
        
        # the dfs method will do a guardian check to see if we are out of bounds or not processing a valid square
        # else we update the current cell to be a '0' to not process it again, and we continue the dfs to see how much more
        # of a contiguous island we can get
        def dfs(i, j):
            if i < 0 or j < 0 or j >= n or i >= m or grid[i][j] != "1":
                return
            grid[i][j] = "0"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        # we need to find a valid starting points for our DFS, each time we do so, we increment the number of islands by 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)
        
        return islands
    # Run Time: O(M * N)
        