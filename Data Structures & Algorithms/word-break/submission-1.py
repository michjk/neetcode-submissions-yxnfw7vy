class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for word in wordDict:
                n_word = len(word)
                if i - n_word < 0:
                    continue
                if s[i - n_word:i] == word:
                    dp[i] |= dp[i - n_word]
        print(dp)
        return dp[n]