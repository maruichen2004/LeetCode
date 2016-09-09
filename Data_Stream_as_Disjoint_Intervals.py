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
        self.heap = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        self.heap.append([val, val])

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        if len(self.heap) == 0:
            return []
        heapq.heapify(self.heap)
        res = [heapq.heappop(self.heap)]
        while self.heap:
            start, end = heapq.heappop(self.heap)
            if start > res[-1][1] + 1:
                res.append([start, end])
            else:
                res[-1][1] = max(res[-1][1], end)
        self.heap = res
        return [Interval(i, j) for i, j in res]

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()