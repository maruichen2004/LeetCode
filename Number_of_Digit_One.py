class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        if n <= 0:
            return 0
        if 1 <= n <= 9:
            return 1
        head, level = n, 1
        while head >= 10:
            level *= 10
            head /= 10
        if n / level == 1:
            return self.countDigitOne(level - 1) + self.countDigitOne(n - level) + n - level + 1
        return (n / level) * self.countDigitOne(level - 1) + self.countDigitOne(n - n / level * level) + level
