class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        longest, mid = "", (n - 1 )/2
        i, j = mid, mid
        while i >= 0 and j < n:
            args = [(i, i), (i, i+1), (j, j), (j, j+1)]
            for l, r in args:
                tmp = self.helper(s, l, r)
                if len(tmp) > len(longest):
                    longest = tmp
            if len(longest) >= 2 * i:
                return longest
            i, j = i - 1, j + 1
        return longest
        
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l, r = l - 1, r + 1
        return s[l+1:r]