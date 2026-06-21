class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        stack = []
        res = 0
        for i in range(n):
            while stack and stack[-1][0] <= height[i]:
                cur_h, cur_idx = stack.pop()
                left_h = stack[-1][0] if stack else 0
                left_idx = stack[-1][1] if stack else 0
                h = min(height[i] - cur_h, max(0, left_h - cur_h))
                w = (i - left_idx - 1)
                area = h * w
                res += area
            stack.append((height[i], i))
        return res

