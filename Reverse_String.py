class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = [i for i in s]
        i, j = 0, len(res) - 1
        while i < j:
            res[i], res[j] = res[j], res[i]
            i += 1
            j -= 1
        return ''.join(res)