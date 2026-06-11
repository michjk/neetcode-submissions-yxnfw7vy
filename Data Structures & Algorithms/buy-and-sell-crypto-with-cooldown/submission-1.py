class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]

        for i in range(n):
            # Hold: buy today (need not-holding from i-2) or carry hold from i-1
            buy          = (dp[i - 2][1] - prices[i]) if i >= 2 else -prices[i]
            cooldown_buy = dp[i - 1][0]               if i >= 1 else float('-inf')
            dp[i][0] = max(buy, cooldown_buy)

            # Not hold: sell today (need holding from i-1) or carry not-holding from i-1
            sell          = (dp[i - 1][0] + prices[i]) if i >= 1 else float('-inf')
            cooldown_sell = dp[i - 1][1]               if i >= 1 else 0
            dp[i][1] = max(sell, cooldown_sell)

        return dp[n - 1][1]