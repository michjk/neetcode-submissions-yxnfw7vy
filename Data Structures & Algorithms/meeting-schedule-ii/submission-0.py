"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        
        res = 0
        start_pos = 0
        last_pos = 0

        for start_pos in range(len(intervals)):
            if starts[start_pos] < ends[last_pos]:
                res += 1
            else:
                last_pos += 1

        return res
