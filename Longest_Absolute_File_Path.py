class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        stack = []
        res = 0
        for s in input.split('\n'):
            level = s.rfind('\t') + 1
            while len(stack) != level:
                stack.pop()
            length = len(s[level:])
            if len(stack) == 0:
                stack.append(length)
            else:
                stack.append(stack[-1] + length + 1)
            if '.' in s:
                res = max(res, stack[-1])
        return res