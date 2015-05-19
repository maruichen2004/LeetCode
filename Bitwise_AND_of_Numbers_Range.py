ass Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        i, diff = 0, n - m
        while diff:
            diff >>= 1
            i += 1
        return n & m >> i << i
