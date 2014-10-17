class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        operators = {"+":operator.add, "-":operator.sub, "*":operator.mul, "/":operator.div}
        stack = []
        for token in tokens:
            if token.isdigit() or token[1:].isdigit():
                stack.append(int(token))
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(operators[token](n2 * 1.0, n1)))
        return stack[-1]
