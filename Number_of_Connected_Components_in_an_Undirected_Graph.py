class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = [[] for i in range(n)]
        visited = [False] * n
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        res = 0
        for i in range(n):
            if visited[i] == False:
                res += 1
                self.dfs(graph, visited, i)
        return res
        
    def dfs(self, graph, visited, i):
        if visited[i]:
            return
        visited[i] = True
        for j in graph[i]:
            self.dfs(graph, visited, j)