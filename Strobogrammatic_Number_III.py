class Solution(object):
    def __init__(self):
        self.res = 0
        self.pairs = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]
        
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        for i in range(len(low), len(high) + 1):
            self.dfs(low, high, ['#'] * i, 0, i - 1)
        return self.res
        
    def dfs(self, low, high, cur, l, r):
        if l > r:
            s = ''.join(cur)
            if len(cur) == len(low) and int(low) > int(s):
                return
            if len(cur) == len(high) and int(s) > int(high):
                return
            self.res += 1
            return
        for p in self.pairs:
            cur[l] = p[0]
            cur[r] = p[1]
            if len(cur) > 1 and cur[0] == '0':
                continue
            if l < r or (l == r and p[0] == p[1]):
                self.dfs(low, high, cur, l + 1, r - 1)