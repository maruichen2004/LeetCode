class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num_stack, str_stack = [], []
        cnt, t = 0, ""
        for i, c in enumerate(s):
            if '0' <= c <= '9':
                cnt = 10 * cnt + int(c)
            elif c == '[':
                num_stack.append(cnt)
                str_stack.append(t)
                cnt, t = 0, ""
            elif c == ']':
                k = num_stack.pop()
                t = str_stack.pop() + t * k
            else:
                t += c
        return t if not str_stack else str_stack.pop()