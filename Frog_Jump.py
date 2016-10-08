class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if len(stones) <= 1:
            return True
        n = len(stones)
        m = collections.defaultdict(set)
        m[0].add(0)
        dp = [0] * n
        k = 0
        for i in range(1, n):
            while dp[k] + 1 < stones[i] - stones[k]:
                k += 1
            for j in range(k, i):
                t = stones[i] - stones[j]
                if t-1 in m[j] or t in m[j] or t+1 in m[j]:
                    m[i].add(t)
                    dp[i] = max(dp[i], t)
        return dp[n-1] > 0