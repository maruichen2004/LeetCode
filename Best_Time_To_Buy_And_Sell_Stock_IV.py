class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        res = 0
        if k >= len(prices):
            for i in range(1, len(prices)):
                res += max(0, prices[i] - prices[i-1])
            return res
        l, g = [0] * (k+1), [0] * (k+1)
        for i in range(1, len(prices)):
            profit = prices[i] - prices[i-1]
            for j in reversed(range(1, k+1)):
                l[j] = max(g[j-1] + max(0, profit), l[j] + profit)
                g[j] = max(g[j], l[j])
        return g[k]