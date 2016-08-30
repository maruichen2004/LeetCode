class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        res = [word]
        self.dfs(word, 0, res)
        return res
        
    def dfs(self, word, pos, res):
        for i in range(pos, len(word)):
            for j in range(1, len(word) - i + 1):
                t = word[:i] + str(j) + word[i+j:]
                res.append(t)
                self.dfs(t, i + 1 + len(str(j)), res)