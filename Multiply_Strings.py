class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0": return "0"
        res = [0] * (len(num1) + len(num2))
        n1 = [int(i) for i in num1]
        n2 = [int(i) for i in num2]
        for i in range(len(n1)):
            tmp = [n1[i] * k for k in n2]
            tmp += [0] * (len(n1) - i - 1)
            for j in range(len(tmp)):
                res[-(j+1)] += tmp[-(j+1)]
            for j in reversed(range(1, len(res))):
                res[j-1] += res[j]/10
                res[j] %= 10
        return "".join([str(i) for i in res]).lstrip("0")
