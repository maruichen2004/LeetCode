class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.mat = [[0 for j in range(self.n + 1)] for i in range(self.m + 1)]
        self.bit = [[0 for j in range(self.n + 1)] for i in range(self.m + 1)]
        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        diff = val - self.mat[row+1][col+1]
        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.bit[i][j] += diff
                j += (j & -j)
            i += (i & -i)
        self.mat[row+1][col+1] = val

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.getSum(row2 + 1, col2 + 1) - self.getSum(row2 + 1, col1) - self.getSum(row1, col2 + 1) + self.getSum(row1, col1)
        
    def getSum(self, row, col):
        ret = 0
        i = row
        while i > 0:
            j = col
            while j > 0:
                ret += self.bit[i][j]
                j -= (j & -j)
            i -= (i & -i)
        return ret

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.update(1, 1, 10)
# numMatrix.sumRegion(1, 2, 3, 4)