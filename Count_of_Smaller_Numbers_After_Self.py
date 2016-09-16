class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res, sorted_nums = [0] * len(nums), []
        for i in reversed(range(len(nums))):
            pos = self.searchInsertPos(sorted_nums, nums[i])
            res[i] = pos
            sorted_nums.insert(pos, nums[i])
        return res
        
    def searchInsertPos(self, nums, target):
        if len(nums) == 0:
            return 0
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = (l + r) / 2
            if nums[mid] < target:
                l = mid
            else:
                r = mid
        if nums[l] >= target:
            return l
        if nums[r] >= target:
            return r
        return len(nums)