class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return n
        l2, l3, l5 = 0, 0, 0
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            dp[i] = min(dp[l2] * 2, dp[l3] * 3, dp[l5] * 5)
            if dp[i] == dp[l2] * 2:
                l2 += 1
            if dp[i] == dp[l3] * 3:
                l3 += 1
            if dp[i] == dp[l5] * 5:
                l5 += 1
        return dp[n-1]
