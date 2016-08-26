class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        visited = [False for i in range(len(nums))]
        res = []
        self.helper(sorted(nums), visited, 0, res, [])
        return res
        
    def helper(self, nums, visited, i, res, cur):
        if i == len(nums):
            res.append(cur)
        else:
            for j in range(len(nums)):
                if visited[j] == False:
                    if j > 0 and nums[j] == nums[j - 1] and visited[j - 1] == 0:
                        continue;
                    visited[j] = True
                    self.helper(nums, visited, i + 1, res, cur + [nums[j]])
                    visited[j] = False