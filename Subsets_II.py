class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res
        
    def dfs(self, nums, i, cur, res):
        res.append(cur)
        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j-1]:
                continue
            self.dfs(nums, j+1, cur + [nums[j]], res)