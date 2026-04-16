from collections import defaultdict
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # return heap(nums, k)
        return segment_tree(nums, k)

def heap(nums: List[int], k: int) -> List[int]:
    cnt = defaultdict(int)
    heap = []

    for i in range(k):
        heapq.heappush(heap, (-nums[i], i))
    res = [-heap[0][0]]

    for i in range(k, len(nums)):
        heapq.heappush(heap, (-nums[i], i))
        while heap and heap[0][1] <= i - k:
            heapq.heappop(heap)
        if heap:
            res.append(-heap[0][0])
    
    return res

class SegmentTree:
    def __init__(self, n, a):
        self.n = n
        while (self.n & (self.n - 1)) != 0:
            self.n += 1
        self.build(n, a)
    
    def build(self, n, a):
        self.tree = [float("-inf")] * (2 * self.n)
        for i in range(n):
            self.tree[self.n + i] = a[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = max(self.tree[i << 1], self.tree[i << 1 | 1])
    
    def query(self, l, r):
        res = float("-inf")
        l += self.n
        r += self.n + 1

        while l < r:
            if l & 1:
                res = max(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = max(res, self.tree[r])
            l >>= 1
            r >>= 1
        return res

def segment_tree(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    sg = SegmentTree(n, nums)
    res = []
    for i in range(n - k + 1):
        res.append(sg.query(i, i + k - 1))
    return res


        