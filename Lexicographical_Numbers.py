class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(1, 10):
            self.dfs(res, i, n)
        return res
        
    def dfs(self, res, i, n):
        if i <= n:
            res.append(i)
            if 10 * i <= n:
                for j in range(10):
                    self.dfs(res, 10 * i + j, n)