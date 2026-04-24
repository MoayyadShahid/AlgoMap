class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # the idea behind permutations is that we have different orderings of a list of numbers
        # the way we do this is by seeing which numbers we have already used and only recursing on the remaining numbers
        n = len(nums)
        res =[]
        sol = []
        used = set()

        def backtrack(i):
            # the depth of our recursion will be the size of the permutation we can generate which is size n
            if i == n:
                res.append(sol[:])
                return
            
            # at each recursion we will go through all the possible numbers in nums, from index 0 to n - 1
            for j in range(n):
                # we must check that the current number we are considering is not already used in our permutation
                if nums[j] not in used:
                    # we add that new number
                    sol.append(nums[j])
                    # we also track that new number as used
                    used.add(nums[j])
                    # now we go onto the next index of our permutation
                    backtrack(i + 1)
                    sol.pop()
                    used.remove(nums[j])
            
        # begin the backtracking
        backtrack(0)
        return res
    # Run Time: O(N * N!)
