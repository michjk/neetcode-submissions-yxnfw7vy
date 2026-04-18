class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for l in range(len(heights) - 1):
            for r in range(l + 1, len(heights)):
                area = (r - l) * min(heights[l], heights[r])
                res = max(res, area)
        
        return res
