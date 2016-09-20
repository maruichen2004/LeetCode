class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, 0, [], res)
        return res
        
    def dfs(self, nums, i, cur, res):
        res.append(cur)
        for j in range(i, len(nums)):
            self.dfs(nums, j+1, cur+[nums[j]], res)