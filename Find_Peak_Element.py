class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) / 2
            if (mid == 0 or nums[mid-1] < nums[mid]) and (mid == len(nums) - 1 or nums[mid] > nums[mid+1]):
                return mid
            elif mid > 0 and nums[mid-1] > nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return l
