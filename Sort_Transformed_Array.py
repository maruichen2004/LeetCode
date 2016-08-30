class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        i, j = 0, len(nums) - 1
        res = [0] * len(nums)
        idx = len(nums) - 1 if a >= 0 else 0
        while i <= j:
            n1, n2 = self.getNumber(nums[i], a, b, c), self.getNumber(nums[j], a, b, c)
            if a >= 0:
                if n1 >= n2:
                    res[idx] = n1
                    idx -= 1
                    i += 1
                else:
                    res[idx] = n2
                    idx -= 1
                    j -= 1
            else:
                if n1 >= n2:
                    res[idx] = n2
                    idx += 1
                    j -= 1
                else:
                    res[idx] = n1
                    idx += 1
                    i += 1
        return res
        
    def getNumber(self, num, a, b, c):
        return a * num * num + b * num + c