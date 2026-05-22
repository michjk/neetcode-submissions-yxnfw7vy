import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            if not dp or dp[-1] < num:
                dp.append(num)
            idx = bisect.bisect_left(dp, num)
            dp[idx] = num
        return len(dp)