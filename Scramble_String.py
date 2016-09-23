class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        n = len(s1)
        dp = [[[False for k in range(n+1)] for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                dp[i][j][1] = s1[i] == s2[j]
        for l in range(2, n+1):
            for i in range(n-l+1):
                for j in range(n-l+1):
                    for k in range(1, l):
                        if (dp[i][j][k] and dp[i+k][j+k][l-k]) or (dp[i+k][j][l-k] and dp[i][j+l-k][k]):
                            dp[i][j][l] = True
                            break
        return dp[0][0][n]