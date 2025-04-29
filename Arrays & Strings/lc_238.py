class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []

        for i in range(len(nums)):
            if i == 0:
                left.append(1)
            else:
                left.append(left[i-1] * nums[i-1])
        
        nums_rev = nums[::-1]
        for i in range(len(nums)):
            if i == 0:
                right.append(1)
            else:
                right.append(right[i-1] * nums_rev[i-1])
        right = right[::-1]

        result = [right[i] * left[i] for i in range(len(nums))]
        return result
