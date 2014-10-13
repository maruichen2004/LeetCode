class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if len(A) == 0: return 0
        low, high = 0, len(A) - 1
        while low <= high:
            mid = (low + high) / 2
            if A[mid] == target: return mid
            elif A[mid] < target: low = mid + 1
            else: high = mid - 1
        if A[mid] > target: return mid
        return mid + 1
