class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum, res = 0, 0
        map = {}
        for i in range(len(nums)):
            sum += nums[i]
            if sum == k:
                res = i + 1
            elif sum - k in map:
                res = max(res, i - map[sum - k])
            if sum not in map:
                map[sum] = i
        return res