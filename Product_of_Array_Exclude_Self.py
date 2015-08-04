class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        if len(nums) < 2:
            return []
        res = [1] * len(nums)
        left, right = 1, 1
        for i in range(len(nums)):
            res[i] *= left
            left *= nums[i]
            res[len(nums) - 1 - i] *= right
            right *= nums[len(nums) - 1 - i]
        return res
