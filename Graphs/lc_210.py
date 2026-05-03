from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
       
       # the idea here is simple, we validate the prerequisites graph, if at any point we have a cycle return empty list
       # otherwise as we keep doing DFS we go to the end of the DFS chain and keep appending courses, where the courses
       # with more pre-reqs or the ones which are dependent will appear at the end as we unravel the DFS

       
        D = defaultdict(list)     
        res = []

        # build the adjacency list, where course u depends on course v
        for u, v in prerequisites:
            D[u].append(v) 

        # applying 3 color strategy
        UNSEEN = 0
        VISITING = 1
        VISITED = 2
        states = [UNSEEN] * numCourses

        # within the DFS we will explore 3 cases
        # 1) if the node we are on is VISITED we dont need to go down that path further, it is already safe
        # 2) otherwise if the node we are on is VISITING it means we ended up back in a loop, failure detected
        # 3) else we mark the current node as VISITING and then we explore the pathways from current node's neighbours
        #    when we run the DFS down those pathways if we have no failures then we can mark the current node as VISITED and return True
        #    also we append that current node to the end of the result list of the prerequisite chain, or the order in which courses can be taken
        def dfs(i):
            if states[i] == VISITED:
                return True
            elif states[i] == VISITING:
                return False
            else:
                states[i] = VISITING
                for nei in D[i]:
                    if not dfs(nei):
                        return False
                res.append(i)
                states[i] = VISITED
                return True

        # we go through each course node and run the DFS on each one to determine whether we have a failure or if we can go through fully then we have result built
        for i in range(numCourses):
            if not dfs(i):
                return []
    
        return res
    # Run Time: O(V + E)
