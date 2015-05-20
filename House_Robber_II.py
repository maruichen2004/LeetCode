class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        return max(self.robRange(nums, 0, len(nums) - 1), self.robRange(nums, 1, len(nums)))
        
    def robRange(self, nums, start, end):
        n, n1 = nums[start], 0
        for i in range(start + 1, end):
            n1, n2 = n, n1
            n = max(nums[i] + n2, n1)
        return n
