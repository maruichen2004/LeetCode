class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        idxs = [0] * len(primes)
        res = [1]
        cur = res[0]
        for i in range(1, n):
            nums = [0] * len(primes)
            for j in range(len(primes)):
                nums[j] = res[idxs[j]] * primes[j]
            cur = min(nums)
            for j in range(len(primes)):
                if cur == nums[j]:
                    idxs[j] += 1
            res.append(cur)
        return res[n-1]