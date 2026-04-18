from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = defaultdict(int)
        cnt[0] = 1
        res = 0
        for i in range(n):
            if i > 0:
                nums[i] += nums[i - 1]
            rem = nums[i] - k
            if rem in cnt:
                res += cnt[rem]
            cnt[nums[i]] += 1
        return res

            
