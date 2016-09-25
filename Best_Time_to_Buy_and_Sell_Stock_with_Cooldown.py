class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        buy, sell = [0] * len(prices), [0] * len(prices)
        buy[0], buy[1] = -prices[0], max(-prices[0], -prices[1])
        sell[0], sell[1] = 0, max(0, prices[1] - prices[0])
        for i in range(2, len(prices)):
            buy[i] = max(sell[i-2] - prices[i], buy[i-1])
            sell[i] = max(buy[i-1] + prices[i], sell[i-1])
        return sell[-1]