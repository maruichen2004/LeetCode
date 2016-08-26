class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        #https://www.youtube.com/watch?v=yCQN096CwWM
        #https://www.quora.com/Given-an-array-of-integers-A-and-an-integer-k-find-a-subarray-that-contains-the-largest-sum-subject-to-a-constraint-that-the-sum-is-less-than-k
        m, n = len(matrix), len(matrix[0])
        res = float('-inf')
        for l in range(n):
            sums = [0] * m
            for r in range(l, n):
                slist, num = [], 0
                for i in range(m):
                    sums[i] += matrix[i][r]
                    num += sums[i]
                    if num <= k: res = max(res, num)
                    idx = bisect.bisect_left(slist, num - k)
                    if idx != len(slist): res = max(res, num - slist[idx])
                    bisect.insort(slist, num)
        return ans or 0