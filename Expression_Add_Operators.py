class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        self.dfs(num, target, 0, 0, "", res)
        return res
        
    def dfs(self, num, target, prevNum, sum, cur, res):
        if len(num) == 0 and sum == target:
            res.append(cur)
        else:
            for i in range(1, len(num)+1):
                newNum = num[:i]
                if len(newNum) > 1 and newNum[0] == '0':
                    return
                if len(cur) > 0:
                    self.dfs(num[i:], target, long(newNum), sum + long(newNum), cur + '+' + newNum, res)
                    self.dfs(num[i:], target, -long(newNum), sum - long(newNum), cur + '-' + newNum, res)
                    self.dfs(num[i:], target, prevNum * long(newNum), sum - prevNum + prevNum * long(newNum), cur + '*' + newNum, res)
                else:
                    self.dfs(num[i:], target, long(newNum), long(newNum), newNum, res)