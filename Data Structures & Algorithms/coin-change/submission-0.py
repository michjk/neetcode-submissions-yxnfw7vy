class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float("inf")] * (n + 1) for _ in range(amount + 1)]
        
        for i in range(1, n + 1):
            dp[0][i] = 0
        
        for i in range(1, amount + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i][j - 1]
                if i >= coins[j - 1]:
                    dp[i][j] = min(dp[i][j], dp[i - coins[j - 1]][j] + 1)

        return dp[amount][n] if dp[amount][n] != float("inf") else -1
        