class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        lst, dict = list(s), {}
        i = 0
        while i + 10 <= len(s):
            key = s[i:i+10]
            if key in dict: dict[key] += 1
            else : dict[key] = 1
            i = i + 1
        lst = [key for key, value in dict.items() if value > 1]
        return lst
