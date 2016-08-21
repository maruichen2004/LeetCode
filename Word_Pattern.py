class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(words) != len(pattern):
            return False
        map1 = {}
        map2 = {}
        for i in range(len(pattern)):
            if pattern[i] not in map1:
                map1[pattern[i]] = words[i]
            elif map1[pattern[i]] != words[i]:
                return False
            if words[i] not in map2:
                map2[words[i]] = pattern[i]
            elif map2[words[i]] != pattern[i]:
                return False
        return True