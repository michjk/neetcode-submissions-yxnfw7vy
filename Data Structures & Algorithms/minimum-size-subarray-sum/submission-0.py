class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        total = 0
        l = 0

        for r in range(len(nums)):
            total += nums[r]
            while l <= r and total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
         
        return res if res != float("inf") else 0