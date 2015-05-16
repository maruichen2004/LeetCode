class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        if len(grid) == 0: return 0
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and visited[i][j] == False:
                    self.dfs(grid, visited, i, j)
                    count += 1
        return count
        
    def dfs(self, grid, visited, i, j):
        if grid[i][j] == "0" or visited[i][j] == True: return
        visited[i][j] = True
        if i != 0: self.dfs(grid, visited, i-1, j)
        if i != len(grid) - 1: self.dfs(grid, visited, i+1, j)
        if j != 0: self.dfs(grid, visited, i, j-1)
        if j != len(grid[0]) - 1: self.dfs(grid, visited, i, j+1)
