class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        lookup = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []
        self.letterCombinationsRec(res, "", lookup, digits)
        return res
        
    def letterCombinationsRec(self, res, cur, lookup, digits):
        if len(digits) == 0: res.append(cur)
        else:
            for letter in lookup[int(digits[0])]:
                self.letterCombinationsRec(res, cur + letter, lookup, digits[1:])
