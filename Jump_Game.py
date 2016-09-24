class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = [0] * len(nums)
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1], nums[i-1]) - 1
            if dp[i] < 0:
                return False
        return dp[len(nums)-1] >= 0