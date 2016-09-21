class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    self.dfs(grid, visited, i, j)
                    count += 1
        return count
        
    def dfs(self, grid, visited, i, j):
        if visited[i][j]:
            return
        visited[i][j] = True
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if not 0 <= x < len(grid) or not 0 <= y < len(grid[0]) or grid[i][j] != '1':
                continue
            self.dfs(grid, visited, x, y)