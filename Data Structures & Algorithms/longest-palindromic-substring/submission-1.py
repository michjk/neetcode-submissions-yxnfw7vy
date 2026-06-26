class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[-1]
        for i in range(len(s) - 1):
            odd = get_palindrom(i, i, s)
            even = get_palindrom(i, i + 1, s)

            if len(odd) > len(res):
                res = odd
            if len(even) > len(res):
                res = even
        return res

def get_palindrom(l, r, s):
    i, j = l, r
    while i >= 0 and j < len(s) :
        if s[i] != s[j]:
            break
        i -= 1
        j += 1
    return s[i + 1: j]
