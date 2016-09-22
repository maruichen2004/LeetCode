class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        res, a, b = 0, 1, 1
        while n > 0:
            res += (n + 8) / 10 * a + (n % 10 == 1) * b
            b += n % 10 * a
            a *= 10
            n /= 10
        return res