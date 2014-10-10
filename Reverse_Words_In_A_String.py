class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        res, word = "", ""
        for ch in s:
            if ch != " ": word += ch
            else:
                if len(word) != 0:
                    if res != "": res = " " + res
                    res = word + res
                    word = ""
        if len(word) != 0:
            if res != "": res = " " + res
            res = word + res
        return res
