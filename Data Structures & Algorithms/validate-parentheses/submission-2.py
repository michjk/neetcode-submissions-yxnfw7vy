class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {"(": ")", "{": "}", "[": "]"}
        for c in s:
            if c in mp.keys():
                stack.append(c)
            if c in mp.values():
                if not stack or mp.get(stack[-1]) != c:
                    return False
                stack.pop()
        return not stack