from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # we'll use DFS + 3-coloring scheme to determine whether each path leads back to a loop, else we are sure that path is safe
        D = defaultdict(list)

        # build the adjacency list (for this case it kinda makes it easier to say for course u we need course v, like u depends on v)
        for u, v in prerequisites:
            D[u].append(v)
        
        # now we will mark each node via 3 states, either UNSEEN or VISITED means we're safe, but if at any point while we are doing DFS
        # we go down a path where we encounter a VISITING that means we have a loop
        UNSEEN = 0
        VISITING = 1
        VISITED = 2
        # since each node is unique, we will store their states in an array
        states = [UNSEEN] * numCourses
        
        # for the dfs, we will do the following:
        #   enter the dfs with a given node/course
        #   check that if we already VISITED that node then that node is safe or within a safe path (meaaning non-cycle path)
        #   otherwise if state is VISITING, meaning we re-encountered the same node/course in the same recusive seqeuence, hence a cycle
        #   else the current node is UNSEEN logically, so what we do is demarcate it as VISITNG, run DFS on its neighbouring nodes
        #   and if there are no problems with the neighbouring nodes, then we dont have any issues, thus we can demarcate the current node as VISITED
        #   logically, by the end of this DFS, all the nodes within this non-cyclical path starting from node would also been marked VISITED
        def dfs(node):
            state = states[node]
            if state == VISITED:
                return True
            elif state == VISITING:
                return False
            
            states[node] = VISITING
            for nei in D[node]:
                if not dfs(nei):
                    return False

            states[node] = VISITED
            return True
        
        # now we go through all possible courses and we run DFS on them by checking their dependencies and if at any point
        # we have it that the DFS returns False or a failure at node 'i' then we return False, else we return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
    # Run Time: O(V + E)
