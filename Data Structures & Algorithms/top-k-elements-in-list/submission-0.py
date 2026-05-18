from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        freq_list = list(freq.items())

        freq_list.sort(key=lambda x: -x[1])

        return [x for x, _ in freq_list[:k]]


