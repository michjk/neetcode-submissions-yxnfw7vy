class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        while i < n and newInterval[1] >= intervals[i][0]:
            min_start = min(newInterval[0], intervals[i][0])
            max_end = max(newInterval[1], intervals[i][1])
            newInterval = [min_start, max_end]
            i += 1

        res.append(newInterval)
        
        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res
