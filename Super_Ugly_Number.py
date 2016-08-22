class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        nums, idx = [1] * len(primes), [0] * len(primes)
        res = [1]
        cur = res[0]
        for i in range(1, n):
            for j in range(len(primes)):
                if nums[j] == cur:
                    nums[j] = res[idx[j]] * primes[j]
                    idx[j] += 1
            cur = min(nums)
            res.append(cur)
        return res[n-1]