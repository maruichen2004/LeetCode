class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        len1, len2 = len(nums1), len(nums2)
        res = []
        i = max(0, k - len2)
        while i <= min(k, len1):
            res = max(res, self.merge(self.maxK(nums1, i), self.maxK(nums2, k-i)))
            i += 1
        return res
        
    def merge(self, nums1, nums2):
        res = []
        while len(nums1) + len(nums2):
            tmp = nums1 if nums1 > nums2 else nums2
            res.append(tmp[0])
            tmp.pop(0)
        return res

    def maxK(self, nums, k):
        drop = len(nums) - k
        res = []
        for num in nums:
            while drop and len(res) and res[-1] < num:
                drop -= 1
                res.pop()
            res.append(num)
        return res[:k]