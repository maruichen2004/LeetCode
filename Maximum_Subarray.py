class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        res, tmp = nums[0], nums[0]
        for i in range(1, len(nums)):
            tmp = max(tmp + nums[i], nums[i])
            res = max(res, tmp)
        return res