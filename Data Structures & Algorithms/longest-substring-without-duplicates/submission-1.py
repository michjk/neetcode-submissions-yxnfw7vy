class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = len(s) - 1
        unique = set()
        res = 0
        for r in range(len(s)):
            while s[r] in unique:
                unique.remove(s[l])
                l += 1
            res = max(res, r - l + 1)
            unique.add(s[r])
        return res
            