class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False] * n
        dp[0] = True
        left = 0
        for i in range(n):
            if not dp[i]:
                continue
            left = max(left, i + minJump)
            right = min(i + maxJump + 1, n)
            while left < right:
                if s[left] == '0':
                    dp[left] = True
                left += 1

        return dp[n - 1]