class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        res, i = sys.maxint, -1
        for j in range(len(words)):
            if words[j] == word1 or words[j] == word2:
                if i != -1 and words[i] != words[j]:
                    res = min(res, j - i)
                i = j
        return res