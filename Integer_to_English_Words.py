class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = self.convertHundred(num%1000)
        l = ["Thousand", "Million", "Billion"]
        for i in range(3):
            num /= 1000
            res = self.convertHundred(num%1000) + " " + l[i] + " " + res if num % 1000 else res
        if len(res) == 0:
            return "Zero"
        return res.strip()
        
    def convertHundred(self, num):
        l1 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        l2 = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        res = ""
        a, b, c=  num/100, num%100, num%10
        res = l1[b] if b < 20 else l2[b/10] + (" " + l1[c] if c else "")
        if a > 0:
            res = l1[a] + " Hundred" + (" " + res if b else "")
        return res