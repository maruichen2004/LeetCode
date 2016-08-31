class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        dp = [[[0, 0] for j in range(len(grid[0]))] for i in range(len(grid))]
        for i in xrange(0, len(grid)):
            for j in xrange(0, len(grid[0])):
                if grid[i][j] == "E":
                    dp[i][j] = [dp[i - 1][j][0] + 1,  + dp[i][j - 1][1] + 1]
                elif grid[i][j] == "0":
                    dp[i][j] = [dp[i - 1][j][0], dp[i][j - 1][1]]
        maxKilled = 0
        for i in reversed(xrange(0, len(grid))):
            for j in reversed(xrange(0, len(grid[0]))):
                if j != len(grid[0]) - 1:
                    if grid[i][j + 1] != "W":
                        dp[i][j][1] = dp[i][j + 1][1]
                if i != len(grid) - 1:
                    if grid[i + 1][j] != "W":
                        dp[i][j][0] = dp[i + 1][j][0]
                if grid[i][j] == "0":
                    curKilled = dp[i][j][0] + dp[i][j][1]
                    if curKilled > maxKilled:
                        maxKilled = curKilled 

        return maxKilled