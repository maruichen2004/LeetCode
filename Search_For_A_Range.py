class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first, second = -1, -1
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = (l + r) / 2
            if nums[mid] < target:
                l = mid
            else:
                r = mid
        if nums[l] == target:
            first = l
        elif nums[r] == target:
            first = r
        else:
            return [-1, -1]
        r = len(nums) - 1
        while l + 1 < r:
            mid = (l + r) / 2
            if nums[mid] > target:
                r = mid
            else:
                l = mid
        if nums[r] == target:
            second = r
        elif nums[l] == target:
            second = l
        return [first, second]
