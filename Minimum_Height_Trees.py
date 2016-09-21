class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        graph = collections.defaultdict(list)
        res, degree = [], [0] * n
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
            degree[start] += 1
            degree[end] += 1
        q = []
        for i, d in enumerate(degree):
            if d == 1:
                q.append(i)
        while n > 2:
            size = len(q)
            for i in range(size):
                t = q.pop(0)
                n -= 1
                for j in graph[t]:
                    degree[j] -= 1
                    if degree[j] == 1:
                        q.append(j)
        while q:
            res.append(q.pop(0))
        return res