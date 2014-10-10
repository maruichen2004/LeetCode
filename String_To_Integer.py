class Solution:
    # @return an integer
    def atoi(self, str):
        if len(str) == 0: return 0
        res, i, sign, INT_MAX, INT_MIN = 0, 0, 1, 2147483647, -2147483648
        while i < len(str) and str[i].isspace():
            i += 1
        if str[i] == "-": sign = -1
        if str[i] in "-+": i += 1
        while i < len(str) and str[i].isdigit():
            res = 10 * res + (ord(str[i]) - ord('0')) * sign
            i += 1
        if sign == -1 and res < INT_MIN: return INT_MIN
        if sign == 1 and res > INT_MAX: return INT_MAX
        return res
