class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n - 1, -1, -1):
            new_dp = [False] * (n + 1)
            for op in range(n):
                res = False
                if s[i] == "*":
                    res |= dp[op + 1]
                    if op > 0:
                        res |= dp[op - 1]
                    res |= dp[op]
                elif s[i] == "(":
                    res |= dp[op + 1]
                elif op > 0:
                    res |= dp[op - 1]
                new_dp[op] = res
            dp = new_dp
        
        return dp[0]
                        
