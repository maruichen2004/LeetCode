class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti_diag = 0
        self.size = n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        add = 1 if player == 1 else -1
        self.rows[row] += add
        self.cols[col] += add
        self.diag += add if row == col else 0
        self.anti_diag += add if row == self.size - 1 - col else 0
        if abs(self.rows[row]) == self.size or \
            abs(self.cols[col]) == self.size or \
            abs(self.diag) == self.size or \
            abs(self.anti_diag) == self.size:
                return player
        else:
            return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)