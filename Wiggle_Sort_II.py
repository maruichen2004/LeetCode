class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        tmp = sorted(nums)
        k, j = (len(nums) + 1) / 2, len(nums)
        for i in range(len(nums)):
            if i % 2 == 1:
                j -= 1
                nums[i] = tmp[j]
            else:
                k -= 1
                nums[i] = tmp[k]