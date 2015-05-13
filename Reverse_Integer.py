class Solution:
    # @return an integer
    def reverse(self, x):
        inf = 2**31 - 1
        sign = -1 if x < 0 else 1
        res, num = 0, abs(x)
        while num > 0:
            res = res * 10 + num % 10
            num /= 10
            if res > inf: return 0
        return res * sign
