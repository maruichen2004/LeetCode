class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 0:
            return 0
        n, s, t = len(A), 0, 0
        for i in range(n):
            s += A[i]
            t += i * A[i]
        res = t
        for i in range(1, n):
            t = t + s - n * A[n-i]
            res = max(res, t)
        return res