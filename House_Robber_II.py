class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums, 0, len(nums)-1), self.helper(nums, 1, len(nums)))
        
    def helper(self, nums, l, r):
        if l + 1 == r:
            return nums[l]
        dp = [0] * r
        dp[l], dp[l+1] = nums[l], max(nums[l], nums[l+1])
        for i in range(l+2, r):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[r-1]