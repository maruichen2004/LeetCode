class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        res = []
        self.combinationSumRec(res, [], sorted(candidates), target, 0)
        return res
        
    def combinationSumRec(self, res, cur, candidates, target, i):
        if target == 0 and cur not in res: res.append(cur)
        else:
            while i < len(candidates) and candidates[i] <= target:
                self.combinationSumRec(res, cur + [candidates[i]], candidates, target - candidates[i], i + 1)
                i += 1
