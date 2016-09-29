class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = len(nums1) + len(nums2)
        if total % 2 == 1:
            return self.findK(nums1, nums2, total/2 + 1)
        else:
            return 0.5*(self.findK(nums1, nums2, total/2) + self.findK(nums1, nums2, total/2+1))
            
    def findK(self, nums1, nums2, k):
        if len(nums1) > len(nums2):
            return self.findK(nums2, nums1, k)
        if len(nums1) == 0:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])
        pa = min(k/2, len(nums1))
        pb = k - pa
        if nums1[pa-1] < nums2[pb-1]:
            return self.findK(nums1[pa:], nums2, k - pa)
        elif nums1[pa-1] > nums2[pb-1]:
            return self.findK(nums1, nums2[pb:], k - pb)
        else:
            return nums1[pa-1]