class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix: return 0
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        max_size = 0
        for j in range(len(matrix[0])):
            if matrix[0][j] == '1':
                dp[0][j] = 1
                max_size = max(max_size, dp[0][j])
        for i in range(1, len(matrix)):
            if matrix[i][0] == '1':
                dp[i][0] = 1
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_size = max(max_size, dp[i][j])
                else:
                    dp[i][j] = 0
        return max_size * max_size
