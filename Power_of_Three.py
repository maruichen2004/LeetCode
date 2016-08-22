class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        max = 3 ** 19
        return n > 0 and max % n == 0