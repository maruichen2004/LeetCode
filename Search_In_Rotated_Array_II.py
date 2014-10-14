class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        l, r = 0, len(A) - 1
        while l <= r:
            mid = (l + r) / 2
            if A[mid] == target: return True
            if A[l] < A[mid]:
                if A[l] <= target < A[mid]: r = mid - 1
                else: l = mid + 1
            elif A[mid] < A[l]:
                if A[mid] < target <= A[r]: l = mid + 1
                else: r = mid - 1
            else: l += 1
        return False
