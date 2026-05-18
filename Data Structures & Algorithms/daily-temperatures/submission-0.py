from collections import defaultdict

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = defaultdict(int)
        n = len(temperatures)

        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                top = stack.pop()
                res[top] = i - top
            stack.append(i)
        
        return [res[i] for i in range(n)]
