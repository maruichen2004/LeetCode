class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        self.dfs(num, 0, 0, 0, res)
        return res
        
    def dfs(self, num, i, h, m, res):
        if h > 11 or m > 59:
            return
        if num == 0:
            res.append(str(h) + ':' + '0' * (m < 10) + str(m))
        else:
            for j in range(i, 10):
                if j < 4:
                    self.dfs(num - 1, j + 1, h | (1 << j), m, res)
                else:
                    k = j - 4
                    self.dfs(num - 1, j + 1, h, m | (1 << k), res)