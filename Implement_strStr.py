class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        len1, len2 = len(haystack), len(needle)
        if len2 == 0: return haystack
        if len1 < len2: return None
        for i in range(len1 - len2 + 1):
            j, k = i, 0
            while k < len2:
                if haystack[j] == needle[k]:
                    j, k = j + 1, k + 1
                else: break
            if k == len2: return haystack[i:]
        return None
