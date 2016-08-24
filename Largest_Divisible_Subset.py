class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        dp, parent, res, max_len, max_idx = [0] * len(nums), [0] * len(nums), [], 0, 0
        for i in reversed(range(len(nums))):
            for j in range(i, len(nums)):
                if nums[j] % nums[i] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
                    if dp[i] > max_len:
                        max_len = dp[i]
                        max_idx = i
        for i in range(max_len):
            res.append(nums[max_idx])
            max_idx = parent[max_idx]
        return res