class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        visited = [[0 for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.existRec(board, word, visited, i, j):
                    return True
        return False
        
    def existRec(self, board, word, visited, i, j):
        if len(word) == 0: return True
        if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0 or visited[i][j] == 1 or board[i][j] != word[0]:
            return False
        visited[i][j] = 1
        found = self.existRec(board, word[1:], visited, i - 1, j) or \
                self.existRec(board, word[1:], visited, i + 1, j) or \
                self.existRec(board, word[1:], visited, i, j - 1) or \
                self.existRec(board, word[1:], visited, i, j + 1)
        visited[i][j] = 0
        return found
