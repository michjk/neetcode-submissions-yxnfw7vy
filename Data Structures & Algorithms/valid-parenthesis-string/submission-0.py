class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        dp[n][0] = True

        for i in range(n - 1, -1, -1):
            for op in range(n):
                res = False
                if s[i] == "*":
                    res |= dp[i + 1][op + 1]
                    if op > 0:
                        res |= dp[i + 1][op - 1]
                    res |= dp[i + 1][op]
                elif s[i] == "(":
                    res |= dp[i + 1][op + 1]
                elif op > 0:
                    res |= dp[i + 1][op - 1]
                dp[i][op] = res
        
        return dp[0][0]
                        
