class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        res = []
        self.wordBreakRec(res, "", s, dict)
        return res
        
    def wordBreakRec(self, res, cur, s, dict):
        if self.canBreak(s, dict):
            if len(s) == 0: res.append(cur[1:])
            for i in range(1, len(s) + 1):
                if s[:i] in dict:
                    self.wordBreakRec(res, cur + " " + s[:i], s[i:], dict)
    
    def canBreak(self, s, dict):
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for k in range(i):
                if dp[k] and s[k:i] in dict:
                    dp[i] = True
        return dp[len(s)]
