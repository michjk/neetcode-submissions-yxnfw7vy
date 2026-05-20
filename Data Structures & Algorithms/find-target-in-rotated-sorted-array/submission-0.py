import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        
        idx = bisect.bisect_left(nums, target, lo = left, hi = len(nums))
        if idx < len(nums) and nums[idx] == target:
            return idx
        
        if left > 0:
            idx = bisect.bisect_left(nums, target, lo = 0, hi = left)
            if idx < len(nums) and nums[idx] == target:
                return idx    

        return -1

