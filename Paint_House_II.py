class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0 or len(costs[0]) == 0:
            return 0
        dp = costs
        min1, min2 = -1, -1
        for i in range(len(dp)):
            last1, last2 = min1, min2
            min1, min2 = -1, -1
            for j in range(len(dp[i])):
                if j != last1:
                    dp[i][j] += 0 if last1 < 0 else dp[i-1][last1]
                elif j != last2:
                    dp[i][j] += 0 if last2 < 0 else dp[i-1][last2]
                if min1 < 0 or dp[i][j] < dp[i][min1]:
                    min1, min2 = j, min1
                elif min2 < 0 or dp[i][j] < dp[i][min2]:
                    min2 = j
        return dp[-1][min1]