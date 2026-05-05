"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # if we don't have any nodes, then just return Null / None
        if not node:
            return None

        # the idea here is quite simple, we will use the ptr to the old node, and map it to the ptr of the new clone node
        # that way we will build the new clone graph in a BFS format using a queue

        # intialize the old ptr : new ptr hash map / dict
        clones = {node : Node(node.val)}
        q = deque()
        q.append(node)

        # implement BFS strategy
        while q:
            # we are going to process the current old node
            curr = q.popleft()
            # we will go through the neighbors, and if a neighbor clone exists we won't add it to the BFS queue search, else we will
            for nei in curr.neighbors:
                if nei in clones:
                    clones[curr].neighbors.append(clones[nei])
                else:
                    clones[nei] = Node(nei.val)
                    clones[curr].neighbors.append(clones[nei])
                    q.append(nei)
                
        # 'node' is the starting point of the old graph, so then clones[node] is the starting point of the new graph
        return clones[node]
    
    # Run Time: O(V + E)
