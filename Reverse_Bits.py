class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        table = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
        cur, res, msk = 0, 0, 0xF
        for i in range(8):
            res <<= 4
            cur = msk & n
            res |= table[cur]
            n >>= 4
        return res
