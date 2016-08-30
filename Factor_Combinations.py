class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(n, 2, [], res)
        return res
        
    def dfs(self, n, f, cur, res):
        if cur and n >= f:
            cur.append(n)
            res.append(list(cur))
            cur.pop()
        for i in range(f, int(n**0.5)+1):
            if n % i == 0:
                self.dfs(n/i, i, cur + [i], res)