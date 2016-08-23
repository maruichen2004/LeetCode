class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        map = {}
        for c in magazine:
            if c not in map:
                map[c] = 1
            else:
                map[c] += 1
        for c in ransomNote:
            if c not in map:
                return False
            map[c] -= 1
            if map[c] < 0:
                return False
        return True