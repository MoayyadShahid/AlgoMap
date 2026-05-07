from collections import defaultdict
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    manhat = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    graph[tuple(points[i])].append((manhat, points[j]))
        
        visited = set()
        min_heap = []

        init = tuple(points[0])
        visited.add(init)
        for nei in graph[init]:
            heapq.heappush(min_heap, nei)
        
        cost = 0
        while min_heap and len(visited) != len(points):
            
            small_cost, small_node = heapq.heappop(min_heap)
            small_node = tuple(small_node)
            
            if small_node not in visited:
                cost += small_cost
                visited.add(small_node)
                for nei in graph[small_node]:
                    heapq.heappush(min_heap, nei)


        return cost    
