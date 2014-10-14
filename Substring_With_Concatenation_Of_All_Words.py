class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        res = []
        lenS, lenL, lenW = len(S), len(L), len(L[0])
        for start in range(lenS - lenL * lenW + 1):
            listL = [S[i:i+lenW] for i in range(start, start + lenL * lenW, lenW)]
            found = True
            for item in L:
                if item in listL:
                    listL.remove(item)
                else:
                    found = False
                    break
            if found == True: res.append(start)
        return res
