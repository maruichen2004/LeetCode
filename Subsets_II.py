class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        res = []
        self.subsetsWithDupRec(res, [], sorted(S), 0)
        return res
    
    def subsetsWithDupRec(self, res, cur, S, i):
        if i == len(S) and cur not in res: res.append(cur)
        if i < len(S):
            self.subsetsWithDupRec(res, cur, S, i + 1)
            self.subsetsWithDupRec(res, cur + [S[i]], S, i + 1)
