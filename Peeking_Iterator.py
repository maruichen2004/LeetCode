# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.p_flag = False
        self.p_val = None
        self.itr = iterator

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.p_flag:
            self.p_val = self.itr.next()
            self.p_flag = True
        return self.p_val

    def next(self):
        """
        :rtype: int
        """
        if not self.p_flag:
            return self.itr.next()
        self.p_flag = False
        return self.p_val

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.p_flag:
            return True
        if self.itr.hasNext():
            return True
        return False

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].