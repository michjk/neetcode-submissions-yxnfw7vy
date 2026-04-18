from itertools import accumulate
from operator import mul

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = list(accumulate(nums, mul))
        suffix = list(accumulate(nums[::-1], mul))[::-1]

        res = []
        for i in range(n):
            left = 1
            if i > 0:
                left = prefix[i - 1]
            right = 1
            if i < n - 1:
                right = suffix[i + 1]
            res.append(left * right)
        return res
