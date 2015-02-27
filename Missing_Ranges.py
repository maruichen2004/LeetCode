class Solution:
   def findMissingRanges(self, A, start, end):
      res = []
      prev = start - 1
      for i in range(len(A)):
         cur = end + 1 if i == len(A) else A[i]
         if cur - prev >= 2: res.append(self.getRange(prev + 1, cur - 1))
         prev = cur
      return res

   def getRange(self, from, to):
      if from == to: return str(from)
      else: return str(from) + "->" + str(to)
