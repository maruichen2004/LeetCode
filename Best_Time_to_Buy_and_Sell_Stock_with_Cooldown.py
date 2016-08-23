class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy, pre_buy, sell, pre_sell = -sys.maxint, 0, 0, 0
        for price in prices:
            pre_buy = buy
            buy = max(pre_sell - price, pre_buy)
            pre_sell = sell
            sell = max(pre_buy + price, pre_sell)
        return sell