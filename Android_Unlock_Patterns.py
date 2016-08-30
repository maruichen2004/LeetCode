class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = 0
        visited = [False] * 10
        jumps = [[0 for i in range(10)] for j in range(10)]
        jumps[1][3] = 2; jumps[3][1] = 2
        jumps[4][6] = 5; jumps[6][4] = 5
        jumps[7][9] = 8; jumps[9][7] = 8
        jumps[1][7] = 4; jumps[7][1] = 4
        jumps[2][8] = 5; jumps[8][2] = 5
        jumps[3][9] = 6; jumps[9][3] = 6
        jumps[1][9] = 5; jumps[9][1] = 5; jumps[3][7] = 5; jumps[7][3] = 5
        res += self.dfs(1, 1, 0, m, n, jumps, visited) * 4
        res += self.dfs(2, 1, 0, m, n, jumps, visited) * 4
        res += self.dfs(5, 1, 0, m, n, jumps, visited)
        return res
        
    def dfs(self, num, length, res, m, n, jumps, visited):
        if length >= m:
            res += 1
        length += 1
        if length > n:
            return res
        visited[num] = True
        for next in range(1, 10):
            jump = jumps[num][next]
            if not visited[next] and (jump == 0 or visited[jump]):
                res = self.dfs(next, length, res, m, n, jumps, visited)
        visited[num] = False
        return res