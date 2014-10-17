# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if len(intervals) == 0: return []
        intervals.sort(key = lambda x: x.start)
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i].start > res[-1].end:
                res.append(intervals[i])
            else:
                res[-1].end = max(intervals[i].end, res[-1].end)
        return res
