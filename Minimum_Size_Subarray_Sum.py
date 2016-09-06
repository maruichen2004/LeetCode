class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start, sum, res = 0, 0, len(nums) + 1
        for end in range(len(nums)):
            sum += nums[end]
            while sum >= s:
                res = min(res, end - start + 1)
                sum -= nums[start]
                start += 1
        if res == len(nums) + 1:
            return 0
        return res