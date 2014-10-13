class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        res = [-1, -1]
        low, high = 0, len(A) - 1
        while low < high:
            mid = (low + high) / 2
            if A[mid] == target: high = mid
            elif A[mid] > target: high = mid - 1
            else: low = mid + 1
        if A[low] != target: return res
        res[0] = low
        high = len(A) - 1
        while low < high:
            mid = (low + 1 + high) / 2
            if A[mid] == target: low = mid
            else: high = mid - 1
        res[1] = low
        return res
