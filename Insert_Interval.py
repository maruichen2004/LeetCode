# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        i = 0
        while i < len(intervals):
            if newInterval.start > intervals[i].end:
                i += 1
            elif newInterval.end < intervals[i].start:
                intervals.insert(i, newInterval)
                return intervals
            else:
                newInterval.start = min(newInterval.start, intervals[i].start)
                newInterval.end = max(newInterval.end, intervals[i].end)
                intervals.remove(intervals[i])
        intervals.append(newInterval)
        return intervals
