class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = (l + r) / 2
            if nums[mid] < nums[mid+1]:
                l = mid
            else:
                r = mid
        if (l == 0 or nums[l-1] < nums[l]) and (l == len(nums) - 1 or nums[l] > nums[l+1]):
            return l
        if (r == 0 or nums[r-1] < nums[r]) and (r == len(nums) - 1 or nums[r] > nums[r+1]):
            return r
        return -1
