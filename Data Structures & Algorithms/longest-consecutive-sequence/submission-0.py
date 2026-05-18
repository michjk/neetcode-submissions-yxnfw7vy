class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = set()
        starts = []
        n = len(nums)
        for i in range(n):
            if (nums[i] - 1) not in h:
                starts.append(i)
            h.add(nums[i])
        
        max_n = 0
        for start in starts:
            length = 1
            while (nums[start] + length) in h:
                length += 1
            max_n = max(max_n, length)
        
        return max_n
        


