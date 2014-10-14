class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        left_max, left_maxes, right_max, right_maxes, res = 0, [], 0, [], 0
        for i in range(len(A)):
            left_maxes.append(left_max)
            left_max = max(left_max, A[i])
        for i in reversed(range(len(A))):
            right_maxes.insert(0, right_max)
            right_max = max(right_max, A[i])
        for i in range(len(A)):
            res += max(0, min(left_maxes[i], right_maxes[i]) - A[i])
        return res
