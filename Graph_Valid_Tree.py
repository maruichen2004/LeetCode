class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        visited = [False] * n
        if not self.dfs(graph, visited, 0, -1):
            return False
        for v in visited:
            if not v:
                return False
        return True
        
    def dfs(self, graph, visited, cur, prev):
        if visited[cur]:
            return False
        visited[cur] = True
        for node in graph[cur]:
            if node != prev:
                if not self.dfs(graph, visited, node, cur):
                    return False
        return True