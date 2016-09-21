class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        visited = [False] * (len(nums))
        self.dfs(nums, visited, 0, [], res)
        return res
        
    def dfs(self, nums, visited, i, cur, res):
        if i == len(nums):
            res.append(cur)
        else:
            for j in range(len(nums)):
                if visited[j] == False:
                    visited[j] = True
                    self.dfs(nums, visited, i+1, cur + [nums[j]], res)
                    visited[j] = False