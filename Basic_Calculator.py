ass Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        operands, operators = [], []
        operand = ""
        for i in reversed(range(len(s))):
            if s[i].isdigit():
                operand += s[i]
                if i == 0 or not s[i-1].isdigit():
                    operands.append(int(operand[::-1]))
                    operand = ""
            elif s[i] == ")" or s[i] == "+" or s[i] == "-":
                operators.append(s[i])
            elif s[i] == "(":
                while operators[-1] != ")":
                    self.compute(operands, operators)
                operators.pop()
        while operators:
            self.compute(operands, operators)
        return operands[-1]
        
    def compute(self, operands, operators):
        n1, n2 = operands.pop(), operands.pop()
        op = operators.pop()
        if op == "+":
            operands.append(n1 + n2)
        elif op == "-":
            operands.append(n1 - n2)