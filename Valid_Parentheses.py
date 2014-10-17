class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        for i in s:
            if i in "{[(": stack.append(i)
            else:
                if len(stack) == 0: return False
                elif (i == ")" and stack[-1] != "(") or (i == "]" and stack[-1] != "[") or (i == "}" and stack[-1] != "{"):
                    return False
                else: stack.pop()
        return len(stack) == 0
