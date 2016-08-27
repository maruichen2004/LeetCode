class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.map = collections.defaultdict(list)
        for i, word in enumerate(words):
            self.map[word].append(i)

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        res, i, j = sys.maxint, 0, 0
        while i < len(self.map[word1]) and j < len(self.map[word2]):
            res = min(res, abs(self.map[word1][i] - self.map[word2][j]))
            if self.map[word1][i] < self.map[word2][j]:
                i += 1
            else:
                j += 1
        return res


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")