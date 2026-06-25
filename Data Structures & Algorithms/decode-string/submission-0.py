class Solution:
    def decodeString(self, s: str) -> str:
        str_stack = []
        count_stack = []
        cur = ""
        k = 0

        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                str_stack.append(cur)
                count_stack.append(k)
                cur = ""
                k = 0
            elif c == "]":
                temp = cur
                cur = str_stack.pop()
                count = count_stack.pop()
                cur += temp * count
            else:
                cur += c
        
        return cur