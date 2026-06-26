from collections import defaultdict
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        q = [(-val, idx) for idx, val in enumerate(nums[:k])]
        heapq.heapify(q)
        res = [-q[0][0]]

        for i in range(k, len(nums)):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            res.append(-q[0][0])
        
        return res
