class Solution:
    # @return an integer
    def numTrees(self, n):
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for left in range(i):
                dp[i] += dp[left] * dp[i - left - 1]
        return dp[n]
