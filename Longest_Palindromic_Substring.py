class Solution:
    # @return a string
    def longestPalindrome(self, s):
        longest, mid = "", (len(s) - 1) / 2
        i, j = mid, mid
        while i >= 0 and j < len(s):
            args = [(s, i, i), (s, i, i+1), (s, j, j), (s, j, j+1)]
            for arg in args:
                tmp = self.longestPalindromeSubstr(arg[0], arg[1], arg[2])
                if len(tmp) > len(longest): longest = tmp
            if len(longest) >= 2 * i: return longest
            i, j = i - 1, j + 1
        return longest
        
    def longestPalindromeSubstr(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left, right = left - 1, right + 1
        return s[left+1:right]
