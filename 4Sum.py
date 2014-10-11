class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        if len(num) < 4: return []
        res, A, map = set(), sorted(num), {}
        for p in range(len(A)):
            for q in range(p + 1, len(A)):
                if A[p] + A[q] not in map:
                    map[A[p] + A[q]] = [(p, q)]
                else: 
                    map[A[p] + A[q]].append((p, q))
        for i in range(len(A)):
            for j in range(i + 1, len(A) - 2):
                T = target - A[i] - A[j]
                if T in map:
                    for k in map[T]:
                        if k[0] > j: res.add((A[i], A[j], A[k[0]], A[k[1]]))
        return [list(i) for i in res]
