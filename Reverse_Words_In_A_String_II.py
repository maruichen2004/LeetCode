class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        self.reverse(s, 0, len(s)-1)
        i = 0
        for j in range(len(s) + 1):
            if j == len(s) or s[j] == ' ':
                self.reverse(s, i, j-1)
                i = j + 1
                
    def reverse(self, s, start, end):
        i, j = start, end
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1