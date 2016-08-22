class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        dp = [0] + [sys.maxint] * amount
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i],dp[i-coin] + 1)
                else:
                    break
        return -1 if dp[amount] > amount else dp[amount]