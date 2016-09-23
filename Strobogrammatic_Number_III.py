class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        res = [0]
        for i in range(len(low), len(high) + 1):
            self.dfs(low, high, ['#'] * i, 0, i - 1, res)
        return res[0]
        
    def dfs(self, low, high, cur, l, r, res):
        if l > r:
            s = ''.join(cur)
            if len(cur) == len(low) and int(s) < int(low):
                return
            if len(cur) == len(high) and int(s) > int(high):
                return
            res[0] += 1
            return
        for p, q in [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]:
            cur[l], cur[r] = p, q
            if len(cur) > 1 and cur[0] == '0':
                continue
            if l < r or (l == r and p == q):
                self.dfs(low, high, cur, l+1, r-1, res)