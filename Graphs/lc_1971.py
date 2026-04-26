from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # so we're gonna approach this graph with a BFS, by trying to see if a valid bath exists from the starting
        # node as we branch out to its neighbours and beyond

        # we first check the trivial case where source == destination, if so, we found it
        if source == destination:
            return True

        # now we will store the adjacency list in a hashmap/dictionary <node val, [neighbouring nodes]>
        D = defaultdict(list)
        # we will go through the edges list and since this is a bi-directional/undirected graph, we need to map both u to v and vice versa
        for u, v in edges:
            D[u].append(v)
            D[v].append(u)

        # as for all graphs, we need to make sure we are tracking any cycles and not exploring nodes we've already seen
        seen = set()
        # begin by adding the initial node we are starting from
        seen.add(source)
        # since we are doing BFS, we will need a deque
        dq = deque()
        # enqueue the initial node
        dq.append(source)

        # now we will do our BFS as long as are deque of the nodes we have to explore is not empty
        while dq:
            # our current node we will deal with is popped/dequeued
            curr = dq.popleft()
            # check if the current node is equal to the destination node, if so we have a valid path
            if curr == destination:
                return True
            # otherwise we need to go through the current node's neighbours and explore them
            for nei_node in D[curr]:
                # since we don't want repeats / infinite cycles, we need to see if the neighbour that we will potentially explore has NOT been seen so far
                if nei_node not in seen:
                    # add the new neighbour node to the set and enqueue it into the deque
                    seen.add(nei_node)
                    dq.append(nei_node)
        
        # if after doing our BFS we haven't found the destination node, then we have no valid path
        return False
    
    # Run Time: O(V + E), where V is # of vertices and E is # of edges
