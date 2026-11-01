"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
"""

thoughts (2)
 the curr + 1 interval's start - the curr interval's end >=0

thoughts (3)
intervals are sorted based on start time but we check based on end time if they are consecutive or not?

thoughts(3)
conflict = start interval within curr interval 

thoughts (4)
sort intervals by start time
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        for i in range(len(sorted_intervals)-1):
            if sorted_intervals[i+1].start - sorted_intervals[i].end < 0:
                return False
        return True

