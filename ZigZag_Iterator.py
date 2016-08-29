class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.arrays = [v1, v2]
        self.queue = []
        if v1:
            self.queue.append((v1[0], 0, 0))
        if v2:
            self.queue.append((v2[0], 0, 1))

    def next(self):
        """
        :rtype: int
        """
        val, elem_idx, array_idx = self.queue.pop(0)
        if elem_idx + 1 < len(self.arrays[array_idx]):
            self.queue.append((self.arrays[array_idx][elem_idx+1], elem_idx+1, array_idx))
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.queue) > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())