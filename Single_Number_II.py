class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        bits = [0] * 32
        res = 0
        for x in A:
            for i in range(32):
                if x & (1 << i) == 1 << i: bits[i] += 1
        if bits[31] % 3 == 0:
            for i in range(31):
                if bits[i] % 3 == 1: res += 1 << i
        else:
            for i in range(31):
                if bits[i] % 3 == 0: res += 1 << i
            res = -(1 + res)
        return res
