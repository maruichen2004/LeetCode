class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        if len(words) == 0:
            return []
        dict = {w:i for i, w in enumerate(words)}
        res = []
        for w in dict:
            i = dict[w]
            for j in range(len(w)):
                s1, s2 = w[:j], w[j:]
                if s1 == s1[::-1] and s2[::-1] in dict and dict[s2[::-1]] != i:
                    res.append([dict[s2[::-1]], i])
                if s2 == s2[::-1] and s1[::-1] in dict and dict[s1[::-1]] != i:
                    res.append([i, dict[s1[::-1]]])
            if w != '' and w == w[::-1] and '' in dict:
                res.append([dict[''], i])
        return res