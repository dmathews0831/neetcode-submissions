"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        busy = {}
        for interval in intervals:
            for i in range(interval.start, interval.end):
                if i in busy:
                    return False
                busy[i] = True
        return True