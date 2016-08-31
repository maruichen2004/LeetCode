class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        dist = [[float('inf') for j in range(n)] for i in range(m)]
        count = [[0 for j in range(n)] for i in range(m)]
        res, blds = float('inf'), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j, dist, m, n, count)
                    blds += 1
        for i in range(m):
            for j in range(n):
                if count[i][j] == blds and dist[i][j] < res:
                    res = dist[i][j]
        return res if res != float('inf') else -1
        
    def bfs(self, grid, i, j, dist, m, n, count):
        visited = [[False for y in range(n)] for x in range(m)]
        visited[i][j] = True
        q = [(i, j, 0)]
        while q:
            i, j, d = q.pop(0)
            if dist[i][j] == float('inf'):
                dist[i][j] = 0
            dist[i][j] += d
            for x, y in [(i-1, j), (i+1, j), (i, j+1), (i, j-1)]:
                if 0<= x < m and 0 <= y < n and not visited[x][y]:
                    visited[x][y] = True
                    if grid[x][y] == 0:
                        q.append((x, y, d+1))
                        count[x][y] += 1