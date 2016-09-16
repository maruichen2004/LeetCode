class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        res = float('inf')
        while l + 1 < r:
            mid = (l + r) / 2
            if nums[mid] > nums[l]:
                res = min(res, nums[l])
                l = mid
            else:
                res = min(res, nums[r])
                r = mid
        return min(res, nums[l], nums[r])