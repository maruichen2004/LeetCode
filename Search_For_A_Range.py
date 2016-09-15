class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l + r) / 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        if nums[l] != target:
            return res
        res[0] = l
        r = len(nums)
        while l < r:
            mid = (l + r) / 2
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        res[1] = l-1
        return res
