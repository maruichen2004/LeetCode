class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) / 2
            idx = self.partition(nums, i, j, mid)
            if idx == k - 1: return nums[idx]
            elif idx < k - 1: i = idx + 1
            else: j = idx - 1
        return -1
        
    def partition(self, A, start, end, p):
        pivot = A[p]
        A[end], A[p] = A[p], A[end]
        idx = start
        for i in range(start, end):
            if A[i] > pivot:
                A[i], A[idx] = A[idx], A[i]
                idx += 1
        A[idx], A[end] = A[end], A[idx]
        return idx
