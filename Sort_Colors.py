class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        i, first_two, last_zero = 0, len(A), -1
        while i < first_two:
            if A[i] == 0:
                last_zero += 1
                A[i], A[last_zero] = A[last_zero], A[i]
            elif A[i] == 2:
                first_two -= 1
                A[i], A[first_two] = A[first_two], A[i]
                i -= 1
            i += 1
