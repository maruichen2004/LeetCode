class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return -1
        map = {}
        for c in s:
            if c not in map:
                map[c] = 1
            else:
                map[c] += 1
        for i, c in enumerate(s):
            if map[c] == 1:
                return i
        return -1