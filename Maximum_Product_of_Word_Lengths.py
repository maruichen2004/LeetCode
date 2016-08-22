class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        mask = [0] * len(words)
        res = 0
        for i in range(len(words)):
            for c in words[i]:
                mask[i] |= 1 << (ord(c) - ord('a'))
        for i in range(len(mask)):
            for j in range(i):
                if mask[i] & mask[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        return res