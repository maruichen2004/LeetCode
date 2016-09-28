class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        size, step, start = 1, 9, 1
        while n > size * step:
            n -= size * step
            step *= 10
            start *= 10
            size += 1
        return int(str(start + (n-1)/size)[(n-1)%size])