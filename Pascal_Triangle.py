class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0: return []
        res, cur = [], [1]
        res.append(cur)
        for i in range(1, numRows):
            next = [1]
            for j in range(i - 1):
                next.append(cur[j] + cur[j + 1])
            next.append(1)
            res.append(next)
            cur = next
        return res
