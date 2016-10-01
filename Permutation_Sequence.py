class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res, k, nums = "", k-1, [i+1 for i in range(n)]
        f = [1] * n
        for i in range(1, n):
            f[i] = f[i-1] * i
        for i in reversed(range(1, n+1)):
            j = k / f[i-1]
            k %= f[i-1]
            res += str(nums[j])
            nums.remove(nums[j])
        return res