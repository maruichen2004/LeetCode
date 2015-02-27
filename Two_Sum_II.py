class Solution:
   def twoSum2(self, A, target):
      if len(A) < 2: return []
      i, j = 0, len(A) - 1
      while i < j:
         if A[i] + A[j] > target: j -= 1
         elif A[i] + A[j] < target: i += 1
         else: return [i+1, j+1]
