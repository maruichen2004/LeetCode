class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        lookup = [[False for j in range(len(s))] for i in range(len(s))]
        mincut = [0 for i in range(len(s))]
        for i in reversed(range(len(s))):
            for j in range(i, len(s)):
                if s[i] == s[j]  and (j - i < 2 or lookup[i + 1][j - 1]):
                    lookup[i][j] = True
        for i in range(len(s)):
            min_so_far = 2**32 - 1
            if lookup[0][i] == False:
                for j in range(i):
                    if lookup[j + 1][i] == True:
                        min_so_far = min(min_so_far, mincut[j] + 1)
            else:
                min_so_far = 0
            mincut[i] = min_so_far
        return mincut[-1]
