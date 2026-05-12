class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        n = len(nums)
        target = total // 2

        dp = [[False] * (n + 1) for _ in range(target + 1)]
        dp[0][0] = True

        for i in range(1, target + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i][j - 1]
                if i >= nums[j - 1]:
                    dp[i][j] |= dp[i - nums[j - 1]][j - 1]
        
        return dp[target][n]