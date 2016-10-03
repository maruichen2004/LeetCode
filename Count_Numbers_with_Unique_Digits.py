class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        res = 0
        for i in range(1, n+1):
            res += self.count(i)
        return res
        
    def count(self, k):
        if k == 1:
            return 10
        res = 9
        i = 9
        while i >= 11 - k:
            res *= i
            i -= 1
        return res