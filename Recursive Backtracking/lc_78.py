class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # the idea here is that we will use i as the index of the number in the nums list
        # each time we have 2 choices either we add that number to the sol subset we are creating or not
        # after we have reached the depth i == n, or exhausted all the numbers in nums, then we have reached the base of
        # the recursive backtracking tree and then we append that sol subset to the res
        n = len(nums)
        res = []
        sol = []

        def backtrack(i):
            # if we reached the end of the nums list then we add what subset we created to the final res list and exit recursion
            if i == n:
                res.append(sol[:])
                return
            
            # case 1, we don't add the number at nums[i]
            backtrack(i + 1)

            # case 2, we DO add the number at nums[i]
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()
        
        # begin backtracking by starting off at index i = 0, or nums[0]
        backtrack(0)
        # return the final List
        return res
    
    # Run Time: O(2^N)
