class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        cur = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            if intervals[i][0] <= cur[1]:
                cur = [
                    min(intervals[i][0], cur[0]),
                    max(intervals[i][1], cur[1])
                ]
            else:
                res.append(cur)
                cur = intervals[i]
        res.append(cur)
        return res
