class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = (l + r) / 2
            if nums[mid] == target:
                return True
            elif nums[mid] > nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid
            elif nums[mid] < nums[l]:
                if nums[mid] < target <= nums[r]:
                    l = mid
                else:
                    r = mid
            else:
                l += 1
        return nums[l] == target or nums[r] == target