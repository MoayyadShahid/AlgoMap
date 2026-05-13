from collections import defaultdict
import heapq as hp

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        heap = [(0, k)]
        smallest = {}

        for time in times:
            u, v, w = time
            adj[u].append([w, v])
        
        while heap:
            weight, node = hp.heappop(heap)
            if node in smallest:
                continue
            smallest[node] = weight

            for wei, nei in adj[node]:
                if nei in smallest:
                    continue
                hp.heappush(heap, [wei + weight, nei])
            
        min_time = 0
        for i in range(1, n + 1):
            if i not in smallest:
                return -1
            min_time = max(smallest[i], min_time)
            
        
        return min_time
    