class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if len(s) == 0: return 0
        count, i = 0, len(s) - 1
        while i >= 0:
            if s[i].isspace():
                if count == 0:
                    i -= 1
                    continue
                else: return count
            else:
                count += 1
                i -= 1
        return count
