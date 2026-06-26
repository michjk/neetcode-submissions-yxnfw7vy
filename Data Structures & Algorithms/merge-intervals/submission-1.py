class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        cur = list(intervals[0])
        res = []
        for l, r in intervals:
            if cur[1] >= l:
                cur[1] = max(cur[1], r)
            else:
                res.append(cur)
                cur = [l, r]
        res.append(cur)
        return res
            