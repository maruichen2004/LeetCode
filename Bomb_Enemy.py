class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[[0, 0] for j in range(n)] for i in range(m)]
        if grid[0][0] == 'E':
            dp[0][0] = [1, 1]
        for i in range(1, m):
            if grid[i][0] == 'E':
                dp[i][0] = [dp[i-1][0][0]+1, 1]
            elif grid[i][0] == '0':
                dp[i][0] = [dp[i-1][0][0], 0]
        for j in range(1, n):
            if grid[0][j] == 'E':
                dp[0][j] = [1, dp[0][j-1][1] +1]
            elif grid[0][j] == '0':
                dp[0][j] = [0, dp[0][j-1][1]]
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 'E':
                    dp[i][j] = [dp[i-1][j][0]+1, dp[i][j-1][1]+1]
                elif grid[i][j] == '0':
                    dp[i][j] = [dp[i-1][j][0], dp[i][j-1][1]]
        res = 0
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if i != m-1:
                    if grid[i+1][j] != 'W':
                        dp[i][j][0] = dp[i+1][j][0]
                if j != n-1:
                    if grid[i][j+1] != 'W':
                        dp[i][j][1] = dp[i][j+1][1]
                if grid[i][j] == '0':
                    res = max(res, dp[i][j][0] + dp[i][j][1])
        return res