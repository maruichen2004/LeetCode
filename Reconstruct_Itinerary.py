class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = {}
        for ticket in tickets:
            if ticket[0] in graph:
                graph[ticket[0]].append(ticket[1])
            else:
                graph[ticket[0]] = [ticket[1]]
            if ticket[1] not in graph:
                graph[ticket[1]] = []
        itinerary = ['JFK']
        self.dfs(graph, itinerary, tickets)
        return itinerary
        
    def dfs(self, graph, cur, tickets):
        dest = graph[cur[-1]]
        dest.sort()
        for i in range(len(dest)):
            d = dest.pop(i)
            cur.append(d)
            self.dfs(graph, cur, tickets)
            if len(cur) == len(tickets) + 1:
                return
            cur.pop()
            dest.insert(i, d)