class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = [[False for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, visited, word, i, j):
                    return True
        return False
        
    def dfs(self, board, visited, word, i, j):
        if len(word) == 0:
            return True
        if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or visited[i][j] or board[i][j] != word[0]:
            return False
        visited[i][j] = True
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if self.dfs(board, visited, word[1:], x, y):
                return True
        visited[i][j] = False
        return False