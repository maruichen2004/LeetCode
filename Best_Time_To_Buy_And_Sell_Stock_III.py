class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        min_price, max_profit, max_profits = 2**32 - 1, 0, []
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
            max_profits.append(max_profit)
        max_price, max_profit_after, max_profit_combine = 0, 0, 0
        for i in reversed(range(len(prices))):
            max_price = max(max_price, prices[i])
            max_profit_after = max(max_profit_after, max_price - prices[i])
            max_profit_combine = max(max_profit_combine, max_profit_after + max_profits[i])
        return max_profit_combine
