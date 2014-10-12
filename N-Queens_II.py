class Solution:
    # @return an integer
    def totalNQueens(self, n):
        return self.totalNQueensRec([], n, 0)
    
    def totalNQueensRec(self, cur, n, i):
        if i == n: return 1
        total = 0
        for j in range(n):
            if j not in cur and self.check(cur, i, j) == True:
                total += self.totalNQueensRec(cur + [j], n, i + 1)
        return total
        
    def check(self, cur, row, col):
        for i in range(len(cur)):
            if abs(row - i) == abs(col - cur[i]):
                return False
        return True
