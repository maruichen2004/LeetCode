class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        strs = [c for c in s]
        i, j, cnt = 0, 0, 0
        while 1:
            while i < len(strs) and strs[i] == ' ':
                i += 1
            if i == len(strs):
                break
            if cnt:
                strs[j] = ' '
                j += 1
            k = j
            while i < len(strs) and strs[i] != ' ':
                strs[j] = strs[i]
                i, j = i + 1, j + 1
            self.reverse(strs, k, j - 1)
            cnt += 1
        strs = strs[:j]
        self.reverse(strs, 0, j-1)
        return ''.join(strs)
        
    def reverse(self, s, l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1