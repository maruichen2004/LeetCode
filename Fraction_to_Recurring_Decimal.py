class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0: return "0"
        res, map = "", {}
        if (numerator < 0) ^ (denominator < 0): res += "-"
        n, d = abs(numerator), abs(denominator)
        res += str(n/d)
        n %= d
        if n: res += "."
        while n:
            if n in map:
                res = res[:map[n]] + "(" + res[map[n]:]
                res += ")"
                return res
            map[n] = len(res)
            n *= 10
            res += str(n/d)
            n %= d
        return res
