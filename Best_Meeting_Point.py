class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = [], []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    row.append(i)
                    col.append(j)
        row.sort()
        col.sort()
        res, i, j = 0, 0, len(row) - 1
        while i < j:
            res += row[j] - row[i]
            res += col[j] - col[i]
            i += 1
            j -= 1
        return res