class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_n, min_n = nums[0], nums[0]
        cur_max, cur_min = 0, 0
        total = 0

        for num in nums:
            cur_max = max(cur_max + num, num)
            cur_min = min(cur_min + num, num)
            total += num
            max_n = max(max_n, cur_max)
            min_n = min(min_n, cur_min)
        return max(max_n, total - min_n) if max_n > 0 else max_n