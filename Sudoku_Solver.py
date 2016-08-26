class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return
        self.dfs(board, 0, 0)
        
    def dfs(self, board, row, col):
        if row == 9:
            return True
        if col >= 9:
            return self.dfs(board, row + 1, 0)
        if board[row][col] == '.':
            for k in range(1, 10):
                board[row][col] = str(k)
                if self.check(board, row, col):
                    if self.dfs(board, row, col + 1):
                        return True
                board[row][col] = '.'
        else:
            return self.dfs(board, row, col + 1)
        return False
            
    def check(self, board, row, col):
        for i in range(len(board)):
            if i != row and board[i][col] == board[row][col]:
                return False
        for j in range(len(board[0])):
            if j != col and board[row][j] == board[row][col]:
                return False
        for i in range(3*(row/3), 3*(row/3)+3):
            for j in range(3*(col/3), 3*(col/3)+3):
                if (i != row or j != col) and board[i][j] == board[row][col]:
                    return False
        return True