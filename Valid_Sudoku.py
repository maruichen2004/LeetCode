class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if len(board) == 0 or len(board[0]) == 0:
            return False
        row = [[False for i in range(len(board[0]))] for j in range(len(board))]
        col = [[False for i in range(len(board[0]))] for j in range(len(board))]
        cell = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if '1' <= board[i][j] <= '9':
                    c = ord(board[i][j]) - ord('1')
                    if row[i][c] or col[c][j] or cell[3*(i/3)+j/3][c]:
                        return False
                    row[i][c] = True
                    col[c][j] = True
                    cell[3*(i/3)+j/3][c] = True
        return True