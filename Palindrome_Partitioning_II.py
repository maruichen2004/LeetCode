class Solution:
    # @param {string} s
    # @return {integer}
    def minCut(self, s):
        isPalindrome = [[False for i in range(len(s))] for j in range(len(s))]
        T = [len(s) - 1 - i for i in range(len(s) + 1)]
        for i in reversed(range(len(s))):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i < 2 or isPalindrome[i+1][j-1]):
                    isPalindrome[i][j] = True
                    T[i] = min(T[i], 1 + T[j+1])
        return T[0]
