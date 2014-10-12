class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        res = []
        self.partitionRec(res, [], s, 0)
        return res
        
    def partitionRec(self, res, cur, s, i):
        if i == len(s): res.append(cur)
        else:
            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j+1]):
                    self.partitionRec(res, cur + [s[i:j+1]], s, j+1)
                    
    def isPalindrome(self, s):
        for i in range(len(s)/2):
            if s[i] != s[-(i+1)]: return False
        return True
