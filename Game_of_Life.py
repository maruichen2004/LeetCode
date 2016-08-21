class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0 or len(board[0]) == 0:
            return
        for i in range(len(board)):
            for j in range(len(board[0])):
                lives = self.liveNeighbors(board, i, j)
                if board[i][j] == 1 and (lives == 2 or lives == 3):
                    board[i][j] = 3
                elif board[i][j] == 0 and lives == 3:
                    board[i][j] = 2
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] >>= 1
    
    def liveNeighbors(self, board, row, col):
        lives = 0
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                    continue
                else:
                    lives += board[i][j] & 0x01
        return lives - board[row][col]