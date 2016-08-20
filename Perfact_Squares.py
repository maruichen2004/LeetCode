class Solution(object):
    dp = [0]
        
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        while len(self.dp) <= n:
            m = len(self.dp)
            val = sys.maxint
            i = 1
            while i * i <= m:
                val = min(val, self.dp[m - i * i] + 1)
                i += 1
            self.dp.append(val)
        return self.dp[n]