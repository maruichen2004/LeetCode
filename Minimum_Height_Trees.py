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
        degree = collections.defaultdict(int)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
            degree[start] += 1
            degree[end] += 1
        q = []
        for i, d in degree.items():
            if d == 1:
                q.append(i)
        while n > 2:
            size = len(q)
            for i in range(size):
                cur = q.pop(0)
                n -= 1
                for node in graph[cur]:
                    degree[node] -= 1
                    if degree[node] == 1:
                        q.append(node)
        return q