from collections import defaultdict
import heapq as hq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # we are utilizing Prim's Algorithm here for Minimum Spanning Tree (MST)

        visited = set()
        heap = []
        hq.heappush(heap, (0, 0))
        cost = 0

        # when we have visited all the nodes then we will have completed our MST
        while len(visited) < len(points):
            # we pop the node at index idx of the points array, and we are ordering the heap by distances
            curr = hq.heappop(heap)
            gap, idx = curr[0], curr[1]
            
            # if the current node hasn't been visited then we will process it
            if idx not in visited:
                # we increment the total cost by the distance of the current node from the previous visited node
                cost += gap
                # we add the new node to visited
                visited.add(idx)
                # we get its coordinates
                xi, yi = points[idx]

                # now we go through all the nodes again
                for z in range(len(points)):
                    # if any node isn't in visited we see the distance from the current node to non-visited neighbors
                    # then we add those neighbours in by distance from current into the heap
                    if z not in visited:
                        xj, yj = points[z]
                        dist = abs(xi - xj) + abs(yi - yj)
                        hq.heappush(heap, (dist, z))

        return cost
    # Run Time: O(N ^ 2 log N)
