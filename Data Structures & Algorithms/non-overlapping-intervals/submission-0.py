class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0

        intervals.sort()
        res = [intervals[0]]
        n = len(intervals)

        for i in range(1, n):
            if intervals[i][0] < res[-1][1]: # cur start < prev end
                if intervals[i][1] < res[-1][1]: # cur end < prev end
                    res[-1] = intervals[i]
            else:
                res.append(intervals[i])
        return n - len(res)
