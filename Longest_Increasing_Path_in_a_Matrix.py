class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        res, m, n = 1, len(matrix), len(matrix[0])
        dp = [[0 for j in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(matrix, dp, i, j))
        return res
        
    def dfs(self, matrix, dp, i, j):
        if dp[i][j]:
            return dp[i][j]
        mx, m, n = 1, len(matrix), len(matrix[0])
        for x, y in [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]:
            if not 0 <= x < m or not 0 <= y < n or not matrix[x][y] > matrix[i][j]:
                continue
            mx = max(mx, 1 + self.dfs(matrix, dp, x, y))
        dp[i][j] = mx
        return mx
            