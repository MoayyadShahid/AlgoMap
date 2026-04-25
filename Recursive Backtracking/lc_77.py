class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        sol = []

        # to get the combintations of the numbers from 1 to n, of size k, we need to do the following
        # at each number d we have abs(k - d) branches we can explore, so we need track the current index i of the combination from 0 <= i <= k
        # and we also need to track the current number we are starting from for the combination
        def backtrack(i, curr_num):
            # if we have reached the max size of the combination, we add that combination
            if i == k:
                res.append(sol[:])
                return
            
            # to generate the proper combinations what we will do is loop through the numbers from curr_num to n and 
            # create our combinations based off that, and then restrict what we can choose from as we keep advancing to upper numbers
            for j in range(curr_num, n + 1):
                sol.append(j)
                backtrack(i + 1, j + 1)
                sol.pop()
    
        # begin backtracking
        backtrack(0, 1)
        return res
    # Run Time: O(K * N choose K)
