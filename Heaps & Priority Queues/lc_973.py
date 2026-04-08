import math
import heapq as hp

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # nested helper method to calculate euclidean distance
        def dist(point):
            return math.sqrt(point[0] ** 2 + point[1] ** 2)
        
        # list to serve as the heap
        heap = []

        # create the list for the heap, by having tuples of (distance, point list)
        for i in points:
            line = dist(i)
            heap.append((line, i))
        
        # turn the list into a heap using heapify
        hp.heapify(heap)
        output = []

        # remove the first K elements out of the min heap and append to output list
        for i in range(k):
            minn = hp.heappop(heap)
            output.append(minn[1])
        
        # return the output list
        return output
    # Run Time: O(N)
