class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        lookup = {}
        while n != 1 and n not in lookup:
            lookup[n] = True
            n = self.nextNumber(n)
        return n == 1
        
    def nextNumber(self, n):
        res = 0
        for char in str(n):
            res += int(char)**2
        return res
