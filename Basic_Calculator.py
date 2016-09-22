class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        sign = [1, 1]
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                res += sign.pop() * int(s[start:i])
                continue
            if c in "+-(":
                if c == '-':
                    sign.append(sign[-1] * -1)
                else:
                    sign.append(sign[-1])
            elif c == ')':
                sign.pop()
            i += 1
        return res