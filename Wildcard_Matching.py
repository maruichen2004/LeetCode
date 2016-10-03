class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        idxs, idxp, sstar, pstar = 0, 0, -1, -1
        while idxs < len(s):
            if idxp < len(p) and (s[idxs] == p[idxp] or p[idxp] == '?'):
                idxs, idxp = idxs + 1, idxp + 1
            elif idxp < len(p) and p[idxp] == '*':
                sstar, pstar = idxs, idxp
                idxp += 1
            elif pstar != -1:
                idxp = pstar + 1
                sstar += 1
                idxs = sstar
            else:
                return False
        while idxp < len(p) and p[idxp] == '*':
            idxp += 1
        return idxp == len(p)