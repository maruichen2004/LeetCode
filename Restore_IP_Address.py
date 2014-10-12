class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        res = []
        self.restoreIpAddressesRec(res, "", s, 0)
        return res
        
    def restoreIpAddressesRec(self, res, cur, s, dots):
        if (4 - dots) * 3 < len(s): return
        if dots == 3:
            if self.isValid(s): res.append(cur + s)
        else:
            for i in range(3):
                if len(s) > i and self.isValid(s[:i+1]):
                    self.restoreIpAddressesRec(res, cur + s[:i+1] + ".", s[i+1:], dots + 1)
    
    def isValid(self, s):
        if len(s) == 0 or (s[0] == "0" and s != "0"):
            return False
        return int(s) < 256
