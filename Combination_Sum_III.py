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
        if n < 0:
            return
        if len(cur) == k and n == 0:
            res.append(cur)
        else:
            for j in range(i, 10):
                self.dfs(k, n-j, j+1, cur + [j], res)