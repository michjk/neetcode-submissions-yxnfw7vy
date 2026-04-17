class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[-1]
        cur = 0
        for num in nums:
            cur = cur + num
            res = max(res, cur)
            if cur < 0:
                cur = 0
        return res