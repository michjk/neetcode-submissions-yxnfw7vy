"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from functools import cmp_to_key

def compare_items(a, b):
    
    if a.start != b.start:
        return a.end - b.end
    return a.start - b.start


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        
        intervals = sorted(intervals, key=cmp_to_key(compare_items))
        for i in range(1, len(intervals)):
            if intervals[i - 1].end > intervals[i].start:
                return False

        return True    