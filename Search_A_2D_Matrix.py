class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(matrix) - 1
        row = 0
        while l + 1 < r:
            mid = (l + r) / 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                r = mid
            else:
                l = mid
        if matrix[l][0] <= target <= matrix[l][-1]:
            row = l
        if matrix[r][0] <= target <= matrix[r][-1]:
            row = r
        l, r = 0, len(matrix[0]) - 1
        while l + 1 < r:
            mid = (l + r) / 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid
            else:
                r = mid
        return matrix[row][l] == target or matrix[row][r] == target
