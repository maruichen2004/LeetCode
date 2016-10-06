class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = collections.defaultdict(dict)
        for i, equation in enumerate(equations):
            start, end = equation[0], equation[1]
            graph[start][end] = values[i]
            graph[end][start] = 1.0 / values[i]
            graph[start][start] = 1.0
            graph[end][end] = 1.0
        res = []
        for start, end in queries:
            if start not in graph or end not in graph:
                res.append(-1.0)
            else:
                res.append(self.bfs(graph, start, end))
        return res
        
    def bfs(self, graph, start, end):
        visited = set([start])
        q = [(start, 1.0)]
        while q:
            cur, val = q.pop(0)
            if cur == end:
                return val
            for node in graph[cur]:
                if node not in visited:
                    visited.add(node)
                    q.append((node, val * graph[cur][node]))
        return -1.0