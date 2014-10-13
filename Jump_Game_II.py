class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        if len(A) == 1: return 0
        maxcanreach, jumpnum = 0, 0
        while True:
            jumpnum += 1
            for i in range(maxcanreach + 1):
                maxcanreach = max(maxcanreach, i + A[i])
                if maxcanreach >= len(A) - 1: return jumpnum
