class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.dfs(s, 0, "", res)
        return res
        
    def dfs(self, s, i, cur, res):
        if i == 4:
            if len(s) == 0:
                res.append(cur[:-1])
        else:
            for j in range(1, 4):
                if len(s) < j:
                    break
                val = int(s[:j])
                if val > 255 or len(str(val)) != j:
                    continue
                self.dfs(s[j:], i+1, cur + s[:j] + '.', res)