class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if len(matrix) == 0: return []
        res = []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            for i in range(top + 1, bottom):
                res.append(matrix[i][right])
            for i in reversed(range(left, right + 1)):
                if top < bottom: res.append(matrix[bottom][i])
            for i in reversed(range(top + 1, bottom)):
                if left < right: res.append(matrix[i][left])
            top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1
        return res
