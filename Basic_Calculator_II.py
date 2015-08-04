class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        i, res, sign = 0, 0, 1
        while i < len(s):
            if s[i].isdigit():
                i, preNum = self.getNum(s, i)
                pre = sign * preNum
                res += pre
            elif s[i] in "+-":
                sign = 1 if s[i] == "+" else -1
            elif s[i] in "*/":
                j = i
                res -= pre
                i += 1
                while not s[i].isdigit():
                    i += 1
                i, nextNum = self.getNum(s, i)
                pre = pre * nextNum if s[j] == "*" else sign * (pre / sign / nextNum)
                res += pre
            i += 1
        return res
        
    def getNum(self, s, i):
        j = i
        while i < len(s) and s[i].isdigit():
            i += 1
        i -= 1
        return i, int(s[j:i+1])