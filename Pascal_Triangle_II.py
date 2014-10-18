class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        res = [1]
        for i in range(1, rowIndex + 1):
            next = [1]
            for j in range(i - 1):
                next.append(res[j] + res[j+1])
            next.append(1)
            res = next
        return res
