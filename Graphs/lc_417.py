class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # the idea here is that we will apply DFS on a given graph and see how far from the border nodes can we go into the 
        # graph with monotonically increasing heights
        # we will do this both from the pacific side (left and upper border) and atlantic side (right and lower border)
        # after we do the DFS we will have 2 sets of coordinates of indexes for the pacific side and atlantic side
        # we will apply set intersection to see which nodes from each side are in common, those nodes will be the ones that can drip down into 
        # the atlantic and pacific, then all we have to do is to convert the set elements into a list of sized-2 lists of the indexes
        res = []
        m, n = len(heights), len(heights[0])

        # create the sets
        pacific_visited = set()
        atlantic_visited = set()

        # the dfs will work as follows, if we are beyond the boundaries or if we have already visited the current index or if the current height is less than the previous height we CAN NOT advance
        def dfs(i, j, visited, prev_height):
            if i < 0 or j < 0 or i == m or j == n or (i, j) in visited or heights[i][j] < prev_height :
                return 
            # for each turn of the DFS we add the coordinate pair into the visited set for tracking
            visited.add((i, j))
            # apply DFS in all 4 directions to see how far we can go
            dfs(i - 1, j, visited, heights[i][j])
            dfs(i + 1, j, visited, heights[i][j])
            dfs(i, j - 1, visited, heights[i][j])
            dfs(i, j + 1, visited, heights[i][j])
            
        # this is the DFS for the left and right borders
        for i in range(m):
            dfs(i, 0, pacific_visited, heights[i][0])
            dfs(i, n - 1, atlantic_visited, heights[i][n - 1])
        
        # this is the DFS for the top and bottom borders
        for j in range(n):
                dfs(0, j, pacific_visited, heights[0][j])
                dfs(m - 1, j, atlantic_visited, heights[m - 1][j])
        
        # we apply set intersection
        inter = pacific_visited & atlantic_visited

        # convert each element in the intersection into a list for the final result
        for elem in inter:
            res.append(list(elem))

        return res
    # Run Time: O(V + E) / O(M * N)
