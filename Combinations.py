class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(n, k, [], res)
        return res
        
    def dfs(self, n, k, cur, res):
        if k == 0:
            res.append(cur)
        else:
            for i in reversed(range(1, n+1)):
                if k > i:
                    break
                self.dfs(i-1, k-1, cur+[i], res)