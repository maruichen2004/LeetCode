class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        res = []
        self.solveNQueensRec(res, [], n, 0)
        return res
    
    def solveNQueensRec(self, res, cur, n, i):
        if i == n:
            res.append(map(lambda x: "." * x + "Q" + "." * (n - 1 - x), cur))
        for j in range(n):
            if j not in cur and self.check(cur, i, j) == True:
                self.solveNQueensRec(res, cur + [j], n, i + 1)
    
    def check(self, res, row, col):
        for i in range(len(res)):
            if abs(row - i) == abs(col - res[i]):
                return False
        return True
