class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])
        for i in reversed(range(m-1)):
            dp[i][n-1] = max(1, dp[i+1][n-1] - dungeon[i][n-1])
        for j in reversed(range(n-1)):
            dp[m-1][j] = max(1, dp[m-1][j+1] - dungeon[m-1][j])
        for i in reversed(range(m-1)):
            for j in reversed(range(n-1)):
                dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
        return dp[0][0]