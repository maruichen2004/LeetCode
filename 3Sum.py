class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        if len(num) < 3: return []
        res, A, i = [], sorted(num), 0
        while i < len(A) - 2:
            j, k = i + 1, len(A) - 1
            while j < k:
                if A[i] + A[j] + A[k] == 0:
                    res.append([A[i], A[j], A[k]])
                    j, k = j + 1, k - 1
                    while j < k and A[j] == A[j - 1]: j += 1
                    while k > j and A[k] == A[k + 1]: k -= 1
                elif A[i] + A[j] + A[k] > 0: k -= 1
                else: j += 1
            i += 1
            while i < len(A) - 2 and A[i] == A[i - 1]: i += 1
        return res
