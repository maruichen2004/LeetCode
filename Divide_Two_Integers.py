class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        dividend, divisor = abs(dividend), abs(divisor)
        q = 0
        while dividend >= divisor:
            tmp = divisor
            k = 0
            while dividend >= tmp:
                q += 1 << k
                dividend -= tmp
                tmp <<= 1
                k += 1
        return q * sign
