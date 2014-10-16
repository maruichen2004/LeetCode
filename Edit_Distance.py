class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        dp = [[0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]
        dp[0][0] = 0
        for i in range(1, len(word1) + 1):
            dp[i][0] = dp[i - 1][0] + 1
        for i in range(1, len(word2) + 1):
            dp[0][i] = dp[0][i - 1] + 1
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                addition = dp[i - 1][j] + 1
                deletion = dp[i][j - 1] + 1
                replace = dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]: replace += 1
                dp[i][j] = min(addition, deletion, replace)
        return dp[len(word1)][len(word2)]
