# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        newInterval = Interval(val, val)
        i = 0
        while i < len(self.intervals):
            if newInterval.start > self.intervals[i].end + 1:
                i += 1
            elif newInterval.end + 1 < self.intervals[i].start:
                self.intervals.insert(i, newInterval)
                return
            else:
                newInterval.start = min(newInterval.start, self.intervals[i].start)
                newInterval.end = max(newInterval.end, self.intervals[i].end)
                self.intervals.remove(self.intervals[i])
        self.intervals.append(newInterval)

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()