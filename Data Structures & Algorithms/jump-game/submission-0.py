class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * (n + 1)
        dp[n - 1] = True

        for i in range(n - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                if i + j >= n:
                    break
                dp[i] |= dp[i + j]
        return dp[0]