class Solution:
    # @return a string
    def countAndSay(self, n):
        res = "1"
        for i in range(n - 1):
            next, j = "", 0
            while j < len(res):
                count = 1
                while j < len(res) - 1 and res[j] == res[j+1]:
                    j += 1
                    count += 1
                next += "{0}{1}".format(count, res[j])
                j += 1
            res = next
        return res
