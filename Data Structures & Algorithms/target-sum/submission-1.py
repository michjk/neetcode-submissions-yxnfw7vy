from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}

        def dfs(i, total):
            if i == n:
                if total == target:
                    return 1
                return 0
            key = (i, total)
            
            if key in dp:
                return dp[key]

            dp[key] = dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])
            return dp[key]
        
        return dfs(0, 0)



