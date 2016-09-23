class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        res = []
        self.dfs(s, wordDict, "", res)
        return res
        
    def dfs(self, s, wordDict, cur, res):
        if len(s) == 0:
            res.append(cur[1:])
        else:
            if self.check(s, wordDict):
                for i in range(1, len(s) + 1):
                    if s[:i] in wordDict:
                        self.dfs(s[i:], wordDict, cur + ' ' + s[:i], res)
                        
    def check(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for k in range(i):
                if s[k:i] in wordDict and dp[k]:
                    dp[i] = True
                    break
        return dp[len(s)]