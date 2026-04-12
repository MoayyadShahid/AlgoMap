class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res =[]
        sol = []
        used = set()

        def backtrack(i):
            if i == n:
                res.append(sol[:])
            
            for j in range(n):
                if nums[j] not in used:
                    sol.append(nums[j])
                    used.add(nums[j])
                    backtrack(i + 1)
                    sol.pop()
                    used.remove(nums[j])
            
        backtrack(0)
        return res
