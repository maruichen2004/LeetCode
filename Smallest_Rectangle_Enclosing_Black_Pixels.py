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
        self.dfs(image, visited, x, y, margin)
        return (margin[1] - margin[0] + 1) * (margin[3] - margin[2] + 1)
        
    def dfs(self, image, visited, x, y, margin):
        if not 0 <= x < len(image) or not 0 <= y < len(image[0]) or visited[x][y] or image[x][y] != '1':
            return
        margin[0] = min(margin[0], y)
        margin[1] = max(margin[1], y)
        margin[2] = min(margin[2], x)
        margin[3] = max(margin[3], x)
        visited[x][y] = True
        self.dfs(image, visited, x-1, y, margin)
        self.dfs(image, visited, x+1, y, margin)
        self.dfs(image, visited, x, y+1, margin)
        self.dfs(image, visited, x, y-1, margin)