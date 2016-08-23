class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        cur = {s}
        while True:
            valid = filter(self.isValid, cur)
            if valid:
                return valid
            cur = {s[:i] + s[i+1:] for s in cur for i in range(len(s))}

    def isValid(self, s):
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                cnt -= 1
                if cnt < 0:
                    return False
        return cnt == 0