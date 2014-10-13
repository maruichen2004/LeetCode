class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        reachable = 0
        for i in range(len(A)):
            if reachable < i: return False
            reachable = max(reachable, i + A[i])
        return True
