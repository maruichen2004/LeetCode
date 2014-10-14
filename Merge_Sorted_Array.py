class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        i, j = m - 1, n - 1
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[i + j + 1] = A[i]
                i -= 1
            else:
                A[i + j + 1] = B[j]
                j -= 1
        while j >= 0:
            A[j] = B[j]
            j -= 1
