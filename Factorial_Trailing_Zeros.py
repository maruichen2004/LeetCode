class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        if n <= 0: return 0
        res, d = 0, 5
        while n >= d:
            res += n / d
            d *= 5
        return res
