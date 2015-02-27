class Solution:
   def titleToNumber(self, s):
      n, p = 0, 1
      for i in reversed(range(len(s))):
         n += (ord(s[i]) - ord('A') + 1) * p
         p *= 26
      return n
