class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        For each number x in range[i~j]
        we do: result_when_pick_x = x + max{DP([i~x-1]), DP([x+1, j])}
        --> // the max means whenever you choose a number, the feedback is always bad and therefore leads you to a worse branch.
        then we get DP([i~j]) = min{xi, ... ,xj}
        --> // this min makes sure that you are minimizing your cost.
        '''
        dp = [[0 for i in range(n+1)] for j in range(n+1)]
        for j in range(2, n+1):
            for i in reversed(range(1, j)):
                global_min = sys.maxint
                for k in range(i+1, j):
                    local_max = k + max(dp[i][k-1], dp[k+1][j])
                    global_min = min(global_min, local_max)
                dp[i][j] = i if i + 1 == j else global_min
        return dp[1][n]