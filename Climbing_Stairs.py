class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        dp = [0, 1, 2]
        i = 3
        while i <= n:
            dp.append(dp[i - 1] + dp[i - 2])
            i += 1
        return dp[n]
