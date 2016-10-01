class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        n = len(nums)
        median = heapq.nsmallest(n/2+1, nums)[-1]
        large, small = 1, n-1 if n % 2 == 1 else n-2
        i = small
        while i >= 0:
            if nums[i] < median:
                nums[i], nums[small] = nums[small], nums[i]
                small -= 2
            elif nums[i] > median:
                nums[i], nums[large] = nums[large], nums[i]
                i += 2
                large +=2
            i -= 2
        i = large
        while i < n:
            if nums[i] < median:
                nums[i], nums[small] = nums[small], nums[i]
                i -= 2
                small -= 2
            elif nums[i] > median:
                nums[i], nums[large] = nums[large], nums[i]
                large += 2
            i += 2