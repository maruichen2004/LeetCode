class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if len(s) == 0: return 0
        prev, cur = 0, 1
        for i in range(len(s)):
            tmp = 0
            if s[i] != "0": tmp = cur
            if i > 0 and s[i - 1] != "0" and int(s[i-1:i+1]) < 27:
                tmp += prev
            prev = cur
            cur = tmp
        return cur
