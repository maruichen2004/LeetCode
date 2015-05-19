class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        mapS, mapT = {}, {}
        for i in range(len(s)):
            if s[i] not in mapS:
                mapS[s[i]] = t[i]
            else:
                if mapS[s[i]] != t[i]: return False
            if t[i] not in mapT:
                mapT[t[i]] = s[i]
            else:
                if mapT[t[i]] != s[i]: return False
        return True
