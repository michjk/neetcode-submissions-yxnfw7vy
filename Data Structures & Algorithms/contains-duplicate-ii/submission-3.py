class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_idx = {}
        for i in range(len(nums)):
            if nums[i] in last_idx:
                j = last_idx[nums[i]]
                if nums[i] == nums[j] and i - j <= k:
                    return True
            last_idx[nums[i]] = i
        return False
                