class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.isTerminal = False
        self.leaves = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        cur = self.root
        for c in word:
            if not c in cur.leaves:
                cur.leaves[c] = TrieNode()
            cur = cur.leaves[c]
        cur.isTerminal = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        res, node = self.childSearch(word)
        if res: return node.isTerminal
        return False

    def childSearch(self, word):
        cur = self.root
        for c in word:
            if c in cur.leaves: cur = cur.leaves[c]
            else: return False, None
        return True, cur
        
    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        return self.childSearch(prefix)[0]
# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
