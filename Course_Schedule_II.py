class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(list)
        visited = [0] * numCourses
        res = []
        for cur, pre in prerequisites:
            graph[pre].append(cur)
        for i in range(numCourses):
            if not self.dfs(graph, visited, i, res):
                return []
        return res[::-1]
        
    def dfs(self, graph, visited, i, res):
        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True
        visited[i] = -1
        for cur in graph[i]:
            if not self.dfs(graph, visited, cur, res):
                return False
        res.append(i)
        visited[i] = 1
        return True