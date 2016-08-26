class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        res = ""
        size = 2 * numRows - 2
        for i in range(numRows):
            for j in range(i, len(s), size):
                res += s[j]
                idx = j + size - 2 * i
                if 0 < i < numRows-1 and idx < len(s):
                    res += s[idx]
        return res