class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n

        for i in range(n):
            max_left[i] = left
            left = max(left, height[i]) 
        
        for j in range(n-1, -1, -1):
            max_right[j] = right
            right = max(right, height[j])
        
        sum_rain = 0
        for i in range(n):
            pot = min(max_left[i], max_right[i])
            sum_rain += max(0, pot - height[i])
        return sum_rain
        # Run Time: O(N)
        