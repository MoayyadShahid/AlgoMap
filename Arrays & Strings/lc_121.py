class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr_len = len(prices)
        max = 0
        for i in range(arr_len):
            for j in range(i + 1, arr_len):
                if prices[j] - prices[i] > max:
                    max = prices[j] - prices[i]
        
        return max
        