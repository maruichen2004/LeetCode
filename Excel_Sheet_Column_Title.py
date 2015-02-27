class Solution:
    # @return a string
    def convertToTitle(self, num):
        res = ""
        while num:
            r = num % 26
            num = num / 26
            if r == 0:
                res += "Z"
                num -= 1
            else:
                res += chr(ord('A') + r - 1)
        return res[::-1]
