class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        n = len(s)
        dp = [0] * (n+1)
        res = 0
        for i in range(1, n+1):
            if s[i-1] == '(':
                dp[i] = 0
            else:
                j = i - 2 - dp[i-1]
                if j < 0 or s[j] == ')':
                    dp[i] = 0
                else:
                    dp[i] = dp[j] + dp[i-1] + 2
                    res = max(res, dp[i])
        return res