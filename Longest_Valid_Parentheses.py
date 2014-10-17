class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        longest, last, stack = 0, 0, []
        for i in range(len(s)):
            if s[i] == "(": stack.append(i)
            elif len(stack) == 0: last = i + 1
            else:
                stack.pop()
                if len(stack) == 0: longest = max(longest, i - last + 1)
                else: longest = max(longest, i - stack[-1])
        return longest
