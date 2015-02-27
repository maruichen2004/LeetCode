class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        if len(dungeon) == 0 or len(dungeon[0]) == 0: return 0
        dp = [[0 for i in range(len(dungeon[0]))] for j in range(len(dungeon))]
        for i in reversed(range(len(dungeon))):
            for j in reversed(range(len(dungeon[0]))):
                if i == len(dungeon) - 1 and j == len(dungeon[0]) - 1:
                    dp[i][j] = max(1, 1 - dungeon[i][j])
                else:
                    right = 2**32-1 if j == len(dungeon[0]) - 1 else dp[i][j+1] - dungeon[i][j]
                    down = 2**32-1 if i == len(dungeon) - 1 else dp[i+1][j] - dungeon[i][j]
                    dp[i][j] = max(1, min(down, right))
        return dp[0][0]
