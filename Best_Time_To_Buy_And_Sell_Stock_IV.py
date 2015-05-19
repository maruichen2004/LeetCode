class Solution:
    # @param {integer} k
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, k, prices):
        if k >= len(prices) / 2:
            return self.maxNPairProfit(prices)
        return self.maxKPairProfit(prices, k)
        
    def maxNPairProfit(self, prices):
        profit = 0
        for i in range(len(prices) - 1):
            profit += max(0, prices[i+1] - prices[i])
        return profit
    
    def maxKPairProfit(self, prices, k):
        max_buy = [float("-inf") for i in range(k+1)]
        max_sell = [0 for i in range(k+1)]
        for i in range(len(prices)):
            for j in range(1, min(k, i/2 + 1) + 1):
                max_buy[j] = max(max_buy[j], max_sell[j-1] - prices[i])
                max_sell[j] = max(max_sell[j], max_buy[j] + prices[i])
        return max_sell[k]
