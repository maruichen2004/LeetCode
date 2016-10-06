class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(n, k, [], res, 1)
        return res
        
    def dfs(self, n, k, cur, res, start):
        if len(cur) == k:
            res.append(cur)
        elif n - start + 1 < k - len(cur):
            return
        else:
            for i in range(start, n+1):
                self.dfs(n, k, cur+[i], res, i+1)