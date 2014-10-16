class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for i in range(cols)] for j in range(rows)]
        for i in range(rows):
            if obstacleGrid[i][0] == 0: dp[i][0] = 1
            else: break
        for i in range(cols):
            if obstacleGrid[0][i] == 0: dp[0][i] = 1
            else:break
        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 1: dp[i][j] = 0
                else: dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[rows-1][cols-1]
