class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        res = []
        for i in range(len(input)):
            if input[i] in "+-*":
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for l in left:
                    for r in right:
                        if input[i] == '+':
                            res.append(l + r)
                        elif input[i] == '-':
                            res.append(l - r)
                        elif input[i] == '*':
                            res.append(l * r)
        if len(res) == 0:
            res.append(int(input))
        return res