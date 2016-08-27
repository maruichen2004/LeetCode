class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        prev = lower - 1
        for i in range(len(nums) + 1):
            cur = upper + 1 if i == len(nums) else nums[i]
            if cur - prev >= 2:
                if prev + 1 == cur - 1:
                    res.append(str(prev+1))
                else:
                    res.append(str(prev+1) + '->' + str(cur-1))
            prev = cur
        return res