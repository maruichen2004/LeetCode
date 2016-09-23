class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(k, n, 1, [], res)
        return res
        
    def dfs(self, k, n, i, cur, res):
        if n == 0 and len(cur) == k:
            res.append(cur)
        else:
            for j in range(i, 10):
                if j <= n:
                    self.dfs(k, n-j, j+1, cur + [j], res)