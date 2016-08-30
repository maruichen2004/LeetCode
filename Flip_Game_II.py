class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return False
        for i in range(1, len(s)):
            if s[i] == '+' and s[i-1] == '+' and not self.canWin(s[:i-1] + "--" + s[i+1:]):
                return True
        return False