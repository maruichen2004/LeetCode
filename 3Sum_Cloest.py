class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        res, cloest, A, i = 0, 2**32 - 1, sorted(num), 0
        while i < len(A) - 2:
            j, k = i + 1, len(A) - 1
            while j < k:
                diff = A[i] + A[j] + A[k] - target
                if diff == 0: return target
                elif diff > 0:
                    if abs(diff) < abs(cloest):
                        cloest = diff
                        res = A[i] + A[j] + A[k]
                    k -= 1
                else:
                    if abs(diff) < abs(cloest):
                        cloest = diff
                        res = A[i] + A[j] + A[k]
                    j += 1
            i += 1
        return res
