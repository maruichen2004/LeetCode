class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        res = []
        graph = collections.defaultdict(list)
        for start, end in sorted(tickets)[::-1]:
            graph[start].append(end)
        self.dfs(graph, 'JFK', res)
        return res[::-1]
        
    def dfs(self, graph, airport, res):
        while graph[airport]:
            self.dfs(graph, graph[airport].pop(), res)
        res.append(airport)