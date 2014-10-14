class Solution:
    # @return a list of integers
    def grayCode(self, n):
        res = [0]
        for i in range(n):
            highbit = 1 << i
            for j in reversed(range(len(res))):
                res.append(highbit + res[j])
        return res
