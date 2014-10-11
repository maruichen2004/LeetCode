class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        dict = {x:False for x in num}
        res = -1
        for i in dict:
            if dict[i] == False:
                cur, len1 = i + 1, 0
                while cur in dict:
                    dict[cur] = True
                    cur += 1
                    len1 += 1
                cur, len2 = i - 1, 0
                while cur in dict:
                    dict[cur] = True
                    cur -= 1
                    len2 += 1
                res = max(res, 1 + len1 + len2)
        return res
