class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if len(A) == 0: return 0
        maxSum, tmp = A[0], 0
        for i in range(len(A)):
            tmp = max(tmp + A[i], A[i])
            if tmp > maxSum: maxSum = tmp
        return maxSum
