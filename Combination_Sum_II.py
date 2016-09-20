class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(sorted(candidates), target, 0, [], res)
        return res
        
    def dfs(self, candidates, target, i, cur, res):
        if target < 0:
            return
        if target == 0:
            res.append(cur)
        else:
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                self.dfs(candidates, target - candidates[j], j+1, cur + [candidates[j]], res)