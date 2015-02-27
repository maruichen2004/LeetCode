class Solution:	
    #@param num: A list of non negative integers
    #@return: A string
    def largestNumber(self, num):
        # write your code here
        num.sort(cmp=self.comparator)
        ret = ""
        for n in num: ret += str(n)
        return "0" if ret == '0' * len(num) else ret
       
    def comparator(self, x, y):
        if self.combine(x, y) > self.combine(y, x): return -1
        elif self.combine(x, y) < self.combine(y, x): return 1
        else: return 0
   
    def combine(self, x, y):
        y_digits, tmp_y = 0, y
        while True:
            tmp_y /= 10
            y_digits += 1
            if tmp_y == 0: break
        x *= pow(10, y_digits)
        return x + y
