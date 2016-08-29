class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k
        same, diff = [0] * (n+1), [0] * (n+1)
        same[2] = k
        diff[2] = k * (k - 1)
        for i in range(3, n+1):
            same[i] = diff[i-1]
            diff[i] = (same[i-1] + diff[i-1]) * (k-1)
        return same[n] + diff[n]