class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.flag = False
        
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = TrieNode()
        for word in words:
            self.insert(trie, word)
        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(trie, board, i, j, '', res)
        return res
        
    def insert(self, trie, word):
        node = trie
        for c in word:
            node = node.children[c]
        node.flag = True
        
    def dfs(self, node, board, i, j, word, res):
        if node.flag:
            res.append(word)
            node.flag = False
        elif 0 <= i < len(board) and 0 <= j < len(board[0]):
            char = board[i][j]
            child = node.children.get(char)
            if child is not None:
                board[i][j] = None
                self.dfs(child, board, i+1, j, word+char, res)
                self.dfs(child, board, i-1, j, word+char, res)
                self.dfs(child, board, i, j+1, word+char, res)
                self.dfs(child, board, i, j-1, word+char, res)
                board[i][j] = char