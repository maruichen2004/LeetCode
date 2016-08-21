class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        '''
        if n < 3:
            return True
        dp = [False] * n
        dp[0] = True
        dp[1] = True
        dp[2] = True
        for i in range(3, n):
            dp[i] = not(dp[i-1] and dp[i-2] and dp[i-3])
        return dp[n-1]
        '''
        return bool(n % 4)