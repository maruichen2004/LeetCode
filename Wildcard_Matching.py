class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        idxs, idxp, ss, star = 0, 0, 0, -1
        while idxs < len(s):
            if idxp < len(p) and (p[idxp] == s[idxs] or p[idxp] == "?"):
                idxp, idxs = idxp + 1, idxs + 1
                continue
            if idxp < len(p) and p[idxp] == "*":
                star = idxp
                ss = idxs
                idxp += 1
                continue
            if star != -1:
                idxp = star + 1
                ss += 1
                idxs = ss
                continue
            return False
        while idxp < len(p):
            if p[idxp] != "*": return False
            idxp += 1
        return True
