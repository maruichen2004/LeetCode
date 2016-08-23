class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.insert(0, 1)
        nums.append(1)
        dp = [[0 for j in range(len(nums))] for i in range(len(nums))]
        for l in range(1, n + 1):
            for left in range(1, n + 1 - l + 1):
                right = left + l - 1
                for k in range(left, right + 1):
                    dp[left][right] = max(dp[left][right], nums[left-1] * nums[k] * nums[right+1] + dp[left][k-1] + dp[k+1][right])
        return dp[1][n]