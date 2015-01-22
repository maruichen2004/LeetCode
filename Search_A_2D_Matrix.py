class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0: return False
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m - 1
        while top + 1 < bottom:
            mid = (top + bottom) / 2
            if matrix[mid][0] < target: top = mid
            else: bottom = mid
        if matrix[top][0] <= target <= matrix[top][n-1]: row = top
        elif matrix[bottom][0] <= target <= matrix[bottom][n-1]: row = bottom
        else: return False
        left, right = 0, n-1
        while left + 1 < right:
            mid = (left + right) / 2
            if matrix[row][mid] < target: left = mid
            else: right = mid
        return matrix[row][left] == target or matrix[row][right] == target
