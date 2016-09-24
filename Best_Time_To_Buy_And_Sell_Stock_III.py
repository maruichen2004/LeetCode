class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        l, g = [0] * 3, [0] * 3
        for i in range(len(prices) - 1):
            diff = prices[i+1] - prices[i]
            for j in reversed(range(1, 3)):
                l[j] = max(g[j-1] + max(diff, 0), l[j] + diff)
                g[j] = max(l[j], g[j])
        return g[2]