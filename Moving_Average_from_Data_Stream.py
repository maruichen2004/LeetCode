class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.nums = []
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.nums) < self.size:
            self.nums.append(val)
        else:
            self.nums.pop(0)
            self.nums.append(val)
        return sum(self.nums) * 1.0 / len(self.nums)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)