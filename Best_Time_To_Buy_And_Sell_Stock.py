class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        min_price, max_profit = 2**32 - 1, 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
