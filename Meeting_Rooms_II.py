# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        starts, ends = [], []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        res, endpos = 0, 0
        starts.sort()
        ends.sort()
        for i in range(len(intervals)):
            if starts[i] < ends[endpos]:
                res += 1
            else:
                endpos += 1
        return res