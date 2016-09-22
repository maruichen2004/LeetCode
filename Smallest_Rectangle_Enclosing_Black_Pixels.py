class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        margin = [y, y, x, x]
        visited = [[False for j in range(len(image[0]))] for i in range(len(image))]
        self.dfs(image, margin, visited, x, y)
        return (margin[1] - margin[0] + 1) * (margin[3] - margin[2] + 1)
        
    def dfs(self, image, margin, visited, i, j):
        visited[i][j] = True
        margin[0] = min(margin[0], j)
        margin[1] = max(margin[1], j)
        margin[2] = min(margin[2], i)
        margin[3] = max(margin[3], i)
        for x, y in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
            if not 0 <= x < len(image) or not 0 <= y < len(image[0]) or visited[x][y] or image[x][y] == '0':
                continue
            self.dfs(image, margin, visited, x, y)