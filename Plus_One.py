class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        carry = 0
        for i in reversed(range(len(digits))):
            digits[i] = digits[i] + 1 if i == len(digits) - 1 else digits[i] + carry
            carry = 1 if digits[i] == 10 else 0
            if digits[i] == 10: digits[i] = 0
        if carry == 1: return [1] + digits
        return digits
