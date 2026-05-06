from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # the idea here is that we first do a preliminary check if the rotting is done on T = 0, or if it is not possible at all with no rotten oranges. 
        # after doing guardian checks, we proceed forth by having a queue of starting rotten oranges so that we can run a BFS incrementally by having a tuple of (x, y, minute) so that we can add neighboring fresh oranges into the next minute and continually process multiple rotten oranges within the current minute and get their neighboring fresh oranges
        # at the very end we check if the number of fresh oranges is 0, if not then we have an impossible scenario
        m, n = len(grid), len(grid[0])

        rotten = 0
        fresh = 0
        q = deque()
        for i in range(m):
            for j in range(n):
                # if the current cell has a rotten orange, update rotten counter and add a respective tuple about that rotten orange to the queue
                if grid[i][j] == 2:
                    rotten += 1
                    q.append((i, j, 0))
                # otherwise if it is fresh update fresh counter
                elif grid[i][j] == 1:
                    fresh += 1

        # if we have no fresh oranges, then we finished on minute 0
        if fresh == 0:
            return 0

        # if we have no rotten oranges, the process can't take place thus its impossible
        if rotten == 0: 
            return -1

        curr_time = 0
        while q:
            curr = q.popleft()
            i, j, curr_time = curr[0], curr[1], curr[2]
            
            new_time = curr_time + 1
            # we go through each possible neighboring cell as long as its within bounds
            # we first mark that neighboring cell as rotten, and then append to the queue
            # a tuple demarcating the new rotten orange
            # we also decrement the number of fresh oranges
            if i - 1 >= 0 and grid[i - 1][j] == 1:
                grid[i - 1][j] = 2
                q.append((i - 1, j, new_time))
                fresh -= 1
            if i + 1 < m and grid[i + 1][j] == 1:
                grid[i + 1][j] = 2
                q.append((i + 1, j, new_time))
                fresh -= 1
            if j - 1 >= 0 and grid[i][j - 1] == 1:
                grid[i][j - 1] = 2
                q.append((i, j - 1, new_time))
                fresh -= 1
            if j + 1 < n and grid[i][j + 1] == 1:
                grid[i][j + 1] = 2
                q.append((i, j + 1, new_time))
                fresh -= 1

        # we return the curr time if there are no fresh oranges else we have an impossible case
        return curr_time if fresh == 0 else -1
        
        # Run Time: O(M * N)
