class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        start, sum, min_len = 0, 0, len(nums)
        for i in range(len(nums)):
            sum += nums[i]
            while sum >= s:
                min_len = min(min_len, i - start + 1)
                sum -= nums[start]
                start += 1
        if min_len == len(nums): return 0
        return min_len
