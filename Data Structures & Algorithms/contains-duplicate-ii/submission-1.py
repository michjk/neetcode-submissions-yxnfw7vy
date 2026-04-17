from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        used = set()

        for i in range(min(k + 1, len(nums))):
            if nums[i] in used:
                return True
            used.add(nums[i])
        
        for i in range(k + 1, len(nums)):
            used.remove(nums[i - k - 1])
            if nums[i] in used:
                return True
            used.add(nums[i])
        
        return False

