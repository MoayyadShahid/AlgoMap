class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr_len = len(prices)
        max = 0
        low_p = prices[0]
        for i in range(1, arr_len):
            if prices[i] < low_p:
                low_p = prices[i]
            
            elif prices[i] - low_p > max:
                max = prices[i] - low_p

        return max
