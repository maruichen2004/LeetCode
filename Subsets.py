class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        res = []
        self.subsetsRec(res, [], sorted(S), 0)
        return res
        
    def subsetsRec(self, res, cur, S, i):
        if i == len(S): res.append(cur)
        if i < len(S):
            self.subsetsRec(res, cur, S, i + 1)
            self.subsetsRec(res, cur + [S[i]], S, i + 1)
