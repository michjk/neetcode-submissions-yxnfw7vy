class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        
        for i in range(1, m):
            new_dp = [0] * n
            new_dp[0] = 1
            for j in range(1, n):
                new_dp[j] = dp[j] + new_dp[j - 1]
            dp = new_dp
        return dp[n - 1]