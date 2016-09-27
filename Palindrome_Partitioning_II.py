class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        n = len(s)
        p = [[False for j in range(n)] for i in range(n)]
        dp = [0] * (n+1)
        for i in range(n+1):
            dp[i] = n - 1 - i
        for i in reversed(range(n)):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or p[i+1][j-1]):
                    p[i][j] = True
                    dp[i] = min(dp[i], dp[j+1] + 1)
        return dp[0]