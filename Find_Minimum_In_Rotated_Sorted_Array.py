class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        l, r = 0, len(num) - 1
        while l + 1 < r:
            mid = (l + r) / 2
            if nums[l] < nums[r]: return nums[l]
            if nums[mid] < nums[r]: r = mid
            else: l = mid
        return min(nums[l], nums[r])
