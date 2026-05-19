import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        while left < right:
            mid = left + (right - left) // 2
            hours_needed = sum(math.ceil(pile / mid) for pile in piles)
            
            if hours_needed <= h:
                right = mid  # mid works, try smaller
            else:
                left = mid + 1  # mid too slow, need faster
        
        return left