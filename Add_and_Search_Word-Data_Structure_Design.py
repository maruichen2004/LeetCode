class TrieNode:
    def __init__(self):
        self.isTerminal = False
        self.leaves = {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    
    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.leaves:
                cur.leaves[c] = TrieNode()
            cur = cur.leaves[c]
        cur.isTerminal = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        return self.searchHelper(word, 0, self.root)
        
    def searchHelper(self, word, i, cur):
        if i == len(word): return cur.isTerminal
        if word[i] in cur.leaves: return self.searchHelper(word, i+1, cur.leaves[word[i]])
        elif word[i] == ".":
            for c in cur.leaves:
                if self.searchHelper(word, i+1, cur.leaves[c]): return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
