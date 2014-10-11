class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        lenA, lenB = len(A), len(B)
        if (lenA + lenB) % 2 == 1:
            return self.getMedian(A, B, (lenA + lenB) / 2 + 1)
        else:
            return 0.5 * (self.getMedian(A, B, (lenA + lenB) / 2) + self.getMedian(A, B, (lenA + lenB) / 2 + 1))
            
    def getMedian(self, A, B, k):
        if len(A) > len(B): return self.getMedian(B, A, k)
        if len(A) == 0: return B[k - 1]
        if k == 1: return min(A[0], B[0])
        pa = min(k/2, len(A))
        pb = k - pa
        if A[pa - 1] <= B[pb - 1]: return self.getMedian(A[pa:], B, pb)
        else: return self.getMedian(A, B[pb:], pa)
