class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.map = collections.defaultdict(set)
        for word in dictionary:
            key = word if len(word) <= 2 else word[0] + str(len(word[1:-1])) + word[-1]
            self.map[key] = word if key not in self.map else '' if self.map[key] != word else self.map[key]

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        key = word if len(word) <= 2 else word[0] + str(len(word[1:-1])) + word[-1]
        return key not in self.map or self.map[key] == word

# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")