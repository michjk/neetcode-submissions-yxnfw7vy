class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_2_open = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for c in s:
            if c in close_2_open:
                if stack and stack[-1] == close_2_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack