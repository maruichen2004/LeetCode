class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        idx1, idx2, res = -1, -1, sys.maxint
        for i in range(len(words)):
            if words[i] == word1:
                idx1 = i
            elif words[i] == word2:
                idx2 = i
            if idx1 != -1 and idx2 != -1:
                res = min(res, abs(idx1 - idx2))
        return res