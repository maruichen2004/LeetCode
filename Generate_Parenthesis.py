class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        res = []
        self.generateParenthesisRec(res, "", n, n)
        return res
        
    def generateParenthesisRec(self, res, cur, left, right):
        if left == 0 and right == 0: res.append(cur)
        if left > 0: self.generateParenthesisRec(res, cur + "(", left - 1, right)
        if left < right: self.generateParenthesisRec(res, cur + ")", left, right - 1)
