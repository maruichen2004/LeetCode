class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        if not s: return s
        A = s + s[::-1]
        prefix = self.getPrefix(A)
        return s[prefix[-1]+1:][::-1] + s
        
    def getPrefix(self, s):
        prefix = [-1] * len(s)
        j = -1
        for i in range(1, len(s)):
            while j > -1 and s[j+1] != s[i]:
                j = prefix[j]
            if s[j+1] == s[i]:
                j += 1
            prefix[i] = j
        return prefix
