class TwoSumIII:
   def __init__(self):
      self.dict = {}

   def add(self, num):
      if num in self.dict: self.dict[num] += 1
      else: self.dict[num] = 1

   def find(self, val):
      for key in self.dict.keyset():
         if val - key == key:
            if self.dict[key] >= 2: return True
         elif val - key in self.dict: return True
      return False
