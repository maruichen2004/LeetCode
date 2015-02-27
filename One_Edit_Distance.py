class Solution:
   def isOneEditDistance(self, s, t):
      if len(s) > len(t): return self.isOneEditDistance(t, s)
      if len(t) - len(s) > 1: return False
      i, diff = 0, len(t) - len(s)
      while i < len(s) and s[i] == t[i]: i += 1
      if i == len(s): return diff == 1
      elif diff == 0: i += 1
      while i < len(s) and s[i] == t[i]: i += 1
      return i == len(s)
