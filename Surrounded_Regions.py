class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1:
                    if board[i][j] == 'O':
                        self.dfs(board, i, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '$':
                    board[i][j] = 'O'
    
    def dfs(self, board, i, j):
        board[i][j] = '$'
        for x, y in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
            if 0 < x < len(board) and 0 < y < len(board[0]) and board[x][y] == 'O':
                self.dfs(board, x, y)