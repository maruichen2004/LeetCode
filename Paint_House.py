class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0 or len(costs[0]) == 0:
            return 0
        dp = costs
        for i in range(1, len(costs)):
            dp[i][0] += min(dp[i-1][1], dp[i-1][2])
            dp[i][1] += min(dp[i-1][0], dp[i-1][2])
            dp[i][2] += min(dp[i-1][0], dp[i-1][1])
        return min(dp[-1][0], dp[-1][1], dp[-1][2])