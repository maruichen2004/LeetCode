class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k == len(num):
            return "0"
        stack = []
        i = 0
        while i < len(num):
            while k > 0 and stack and num[i] < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(num[i])
            i += 1
        while k > 0:
            stack.pop()
            k -= 1
        res = ''.join(stack).lstrip('0')
        return "0" if res == "" else res