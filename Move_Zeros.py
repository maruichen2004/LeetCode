class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return
        i = 0
        for j in range(0, len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
        for j in range(i, len(nums)):
            nums[j] = 0