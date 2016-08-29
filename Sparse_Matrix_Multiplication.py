class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [[0 for j in range(len(B[0]))] for i in range(len(A))]
        for i in range(len(A)):
            for k in range(len(A[0])):
                if A[i][k] != 0:
                    for j in range(len(B[0])):
                        if B[k][j] != 0:
                            res[i][j] += A[i][k] * B[k][j]
        return res