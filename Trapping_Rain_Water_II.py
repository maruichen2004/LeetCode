class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if len(heightMap) == 0 or len(heightMap[0]) == 0:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        heap, visited = [], [[False for j in range(n)] for i in range(m)]
        for j in range(n):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            heapq.heappush(heap, (heightMap[m-1][j], m-1, j))
            visited[0][j] = True
            visited[m-1][j] = True
        for i in range(1, m-1):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, (heightMap[i][n-1], i, n-1))
            visited[i][0] = True
            visited[i][n-1] = True
        res = 0
        while heap:
            h, i, j = heapq.heappop(heap)
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    visited[x][y] = True
                    heapq.heappush(heap, (max(h, heightMap[x][y]), x, y))
                    res += max(0, h - heightMap[x][y])
        return res