class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        prev, cur = max(nums[0], nums[1]), nums[0]
        for i in range(2, len(nums)):
            cur, next = prev, cur
            prev = max(nums[i] + next, cur)
        return prev
