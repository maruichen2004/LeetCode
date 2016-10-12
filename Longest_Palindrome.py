class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = set()
        res = 0
        for c in s:
            if c in d:
                d.discard(c)
                res += 1
            else:
                d.add(c)
        return res * 2 + 1 if len(d) > 0 else res * 2