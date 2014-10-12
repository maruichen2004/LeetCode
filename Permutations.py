class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        res = []
        self.permuteRec(res, [], num, 0)
        return res
        
    def permuteRec(self, res, cur, num, i):
        if i == len(num): res.append(cur)
        for j in range(len(num)):
            if num[j] not in cur:
                self.permuteRec(res, cur + [num[j]], num, i + 1)
