class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.small = []
        self.large = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        heapq.heappush(self.small, num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.small) > len(self.large):
            return float(self.small[0])
        return 0.5 * (self.small[0] - self.large[0])
        
# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()