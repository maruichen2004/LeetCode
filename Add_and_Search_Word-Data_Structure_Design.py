class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.flag = False
        
class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            node = node.children[c]
        node.flag = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self._search(self.root, word, 0)

    def _search(self, node, word, i):
        if i == len(word):
            return node.flag
        if word[i] in node.children:
            return self._search(node.children[word[i]], word, i+1)
        else:
            if word[i] == '.':
                for c in node.children:
                    if self._search(node.children[c], word, i+1):
                        return True
        return False
# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")