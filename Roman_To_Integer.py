class Solution:
    # @return an integer
    def romanToInt(self, s):
        singleTable = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        doubleTable = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
        res, i, roman = 0, 0, s.upper()
        while i < len(roman):
            if i < len(roman) - 1 and roman[i:i + 2] in doubleTable:
                res += doubleTable[roman[i:i + 2]]
                i += 2
            elif i < len(roman) and roman[i] in singleTable:
                res += singleTable[roman[i]]
                i += 1
            else:
                return -1
        return res
