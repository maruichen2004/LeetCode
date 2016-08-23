class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res, set1, set2 = [], set(nums1), set(nums2)
        for num in set2:
            if num in set1:
                res.append(num)
        return res