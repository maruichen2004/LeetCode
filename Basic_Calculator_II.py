class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        cur, i, stack, sign = 0, 0, [], '+'
        while i < len(s):
            if s[i].isdigit():
                cur = cur * 10 + int(s[i])
            if s[i] in "+-*/" or i == len(s) - 1:
                if sign == '+':
                    stack.append(cur)
                elif sign == '-':
                    stack.append(-cur)
                elif sign == '*':
                    stack.append(stack.pop() * cur)
                elif sign == '/':
                    prev = stack.pop()
                    if prev < 0:
                        stack.append(-(-prev / cur))
                    else:
                        stack.append(prev / cur)
                sign = s[i]
                cur = 0
            i += 1
        return sum(stack)