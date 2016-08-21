class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for i in range(n)]
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        p1 = self.longestPath(graph, 0)
        p2 = self.longestPath(graph, p1[-1])
        if len(p2) % 2:
            return [p2[len(p2) / 2]]
        else:
            return [p2[len(p2) / 2 - 1], p2[len(p2) / 2]]

    def longestPath(self, graph, root):
        queue = collections.deque([[root]])
        visited = set([root])
        while queue:
            path = queue.popleft()
            for v in graph[path[-1]]:
                if v not in visited:
                    queue.append(path + [v])
                    visited.add(v)
        return path