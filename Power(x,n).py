class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if x == 1 or x == 0 or n == 1: return x
        if n == 0: return 1
        if x == -1:
            if n % 2 == 0: return 1
            else: return -1
        if n < 0: return 1 / self.pow(x, -n)
        val = self.pow(x, n/2)
        if n % 2 == 0: return val * val
        else: return x * val * val
