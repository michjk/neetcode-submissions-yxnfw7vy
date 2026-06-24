class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [0] * (n + 1)
        dp[n - 1] = 1
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j]:
                    dp[j] = 0
                else:
                    dp[j] += dp[j + 1]
        return dp[0]
