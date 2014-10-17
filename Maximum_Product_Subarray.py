class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if len(A) == 0: return 0
        min_local, max_local, res = A[0], A[0], A[0]
        for i in range(1, len(A)):
            tmp = max_local
            max_local = max(A[i] * max_local, A[i] * min_local, A[i])
            min_local = min(A[i] * tmp, A[i] * min_local, A[i])
            res = max(max_local, res)
        return res
