class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        if m == n or m == 0:
            return m
        temp = 1
        while temp < m:
            temp <<= 1
            if m < temp and temp <= n:
                return 0
        ans = m
        for i in xrange(m + 1, n + 1):
            ans = ans & i
        return ans
