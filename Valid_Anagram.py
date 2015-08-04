class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        map = {}
        for c in s:
            if c.lower() in map:
                map[c.lower()] += 1
            else:
                map[c.lower()] = 1
        for c in t:
            if c.lower() in map:
                map[c.lower()] -= 1
                if map[c.lower()] < 0:
                    return False
            else:
                return False
        return True
