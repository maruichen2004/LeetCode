class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        firstRow, firstCol = False, False
        rows, cols = len(matrix), len(matrix[0])
        for i in range(cols):
            if matrix[0][i] == 0:
                firstRow = True
                break
        for i in range(rows):
            if matrix[i][0] == 0:
                firstCol = True
                break
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0, 0
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0: matrix[i][j] = 0
        if firstRow:
            for i in range(cols): matrix[0][i] = 0
        if firstCol:
            for i in range(rows): matrix[i][0] = 0
