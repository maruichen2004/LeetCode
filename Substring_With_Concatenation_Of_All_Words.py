class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0 or len(s) == 0:
            return []
        res = []
        n, m = len(words), len(words[0])
        d1 = collections.defaultdict(int)
        for word in words:
            d1[word] += 1
        for i in range(len(s) - m*n + 1):
            d2 = collections.defaultdict(int)
            j = 0
            while j < n:
                w = s[i+j*m:i+j*m+m]
                if w not in d1:
                    break
                d2[w] += 1
                if d2[w] > d1[w]:
                    break
                j += 1
            if j == n:
                res.append(i)
        return res