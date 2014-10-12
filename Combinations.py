class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        res = []
        self.combineRec(res, [], n, k, 1)
        return res
    
    def combineRec(self, res, cur, n, k, i):
        if len(cur) == k and cur not in res:
            res.append(cur)
        if i <= n:
            self.combineRec(res, cur, n, k, i + 1)
            self.combineRec(res, cur + [i], n, k, i + 1)
