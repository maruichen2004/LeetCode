class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        matrix = [[0 for i in range(n)] for j in range(n)]
        top, bottom, left, right, num = 0, n - 1, 0, n - 1, 1
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            for i in range(top + 1, bottom):
                matrix[i][right] = num
                num += 1
            for i in reversed(range(left, right + 1)):
                if top < bottom:
                    matrix[bottom][i] = num
                    num += 1
            for i in reversed(range(top + 1, bottom)):
                matrix[i][left] = num
                num += 1
            top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1
        return matrix
