class Solution:
    # @return a string
    def getPermutation(self, n, k):
        res, k, fact, perm = "", k - 1, math.factorial(n - 1), [i + 1 for i in range(n)]
        for i in reversed(range(n)):
            cur = perm[k/fact]
            res += str(cur)
            perm.remove(cur)
            if i > 0:
                k %= fact
                fact /= i
        return res
