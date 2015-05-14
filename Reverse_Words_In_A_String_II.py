class Solution:
   def reverseWords(self, s):
      self.reverse(s, 0, len(s))
      i, j = 0, 0
      while j <= len(s):
         if j == len(s) or s[j] == ' ':
            self.reverse(s, i, j)
            i = j + 1
         j += 1

   def reverse(self, s, begin, end):
      for i in range((end - begin)/2):
         s[begin+i], s[end-1-i] = s[end-1-i], s[begin+i]
