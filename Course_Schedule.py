class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        visited = [0] * numCourses
        for cur, pre in prerequisites:
            graph[pre].append(cur)
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True
        
    def dfs(self, graph, visited, i):
        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True
        visited[i] = -1
        for cur in graph[i]:
            if not self.dfs(graph, visited, cur):
                return False
        visited[i] = 1
        return True