class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # the idea here is similar to the leetcode about permutations, where the only change here is we have a running sum (curr_sum)
        res = []
        sol = []
        curr_sum = 0
        # we need to know which numbers we can choose, so we create a set based off candidates to remove duplicatess
        choices = set(candidates)

        def backtrack(i):
            nonlocal curr_sum
            # if the current sum of the numbers we have as our combination is equal to the target then we add that combination 
            if curr_sum == target:
                res.append(sol[:])
                return
            
            # to generate combinations what we need to do is go from the current selected index i and go to the length of candidates
            for j in range(i, len(candidates)):
                # we have a current value given by the current number
                curr_val = candidates[j]
                # if we are still less than or equal to the target after adding the current number, then add it to the combination
                if curr_sum + curr_val <= target:
                    sol.append(curr_val)
                    curr_sum += curr_val
                    # we backtrack on the curent number to explore if we can keep reusing it multiple times
                    backtrack(j)
                    sol.pop()
                    curr_sum -= curr_val
        
        # begin backtracking
        backtrack(0)
        return res
    # Run Time: O(N ^ (T / M)), where N is the size of candidates, T is the value of target, and M is the minimum number
