class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        res, carry = "", 0
        for i in range(max(len(a), len(b))):
            sum = carry
            if i < len(a): sum += int(a[-(i+1)])
            if i < len(b): sum += int(b[-(i+1)])
            carry = sum / 2
            sum %= 2
            res = "{0}{1}".format(sum, res)
        if carry == 1: return "1" + res
        return res
