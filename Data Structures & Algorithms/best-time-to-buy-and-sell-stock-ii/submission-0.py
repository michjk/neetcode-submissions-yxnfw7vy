class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = prices[0]
        n = len(prices)
        
        for i in range(1, n):
            res += max(prices[i] - buy, 0)
            buy = prices[i]
        return res