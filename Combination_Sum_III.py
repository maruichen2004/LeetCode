class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        ret = []
        self.helper(ret, [], 1, k, n)
        return ret
        
    def helper(self, ret, cur, start, k, target):
        if k == 0 and target == 0:
            ret.append(cur)
        elif k < 0: return
        while start < 10 and start * k + k * (k - 1) / 2 <= target:
            self.helper(ret, cur + [start], start + 1, k - 1, target - start)
            start += 1
