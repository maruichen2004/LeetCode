class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        res = [i for i in s]
        i, j = 0, len(res) - 1
        while i < j:
            while i < j and res[i] not in vowels:
                i += 1
            while i < j and res[j] not in vowels:
                j -= 1
            res[i], res[j] = res[j], res[i]
            i += 1
            j -= 1
        return ''.join(res)