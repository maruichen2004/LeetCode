class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        chars = "0123456789abcdef"
        res = ""
        while num != 0:
            res = chars[num & 15] + res
            num = self.rshift(num, 4)
        return res
        
    def rshift(self, val, n):
        return (val % 0x100000000) >> n