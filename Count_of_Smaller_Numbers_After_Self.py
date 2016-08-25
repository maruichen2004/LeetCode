class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res, sorted = [0] * len(nums), []
        for i in reversed(range(len(nums))):
            l, r = 0, len(sorted)
            while l < r:
                mid = (l + r) / 2
                if sorted[mid] >= nums[i]:
                    r = mid
                else:
                    l = mid + 1
            res[i] = r
            sorted.insert(r, nums[i])
        return res