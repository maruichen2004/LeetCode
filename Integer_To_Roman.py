class Solution:
    # @return a string
    def intToRoman(self, num):
        transTable = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
        res = ""
        for trans in sorted(transTable.keys())[::-1]:
            while num >= trans:
                res += transTable[trans]
                num -= trans
            if num == 0: break
        simplifyTable = {"DCCCC":"CM", "CCCC":"CD", "LXXXX":"XC", "XXXX":"XL", "VIIII":"IX", "IIII":"IV"}
        simplifyContent = ["DCCCC", "CCCC", "LXXXX", "XXXX", "VIIII", "IIII"]
        for item in simplifyContent:
            if item in res:
                res = res.replace(item, simplifyTable[item])
        return res
