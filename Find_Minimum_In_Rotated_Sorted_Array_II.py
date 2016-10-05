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
            elif nums[mid] < nums[l]:
                res = min(res, nums[mid])
                r = mid
            else:
                l += 1
        return min(res, nums[l], nums[r])
