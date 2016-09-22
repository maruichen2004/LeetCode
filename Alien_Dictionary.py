class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph = collections.defaultdict(list)
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    graph[a].append(b)
                    break
        indegree = collections.defaultdict(int)
        for src in graph:
            for end in graph[src]:
                indegree[end] += 1
        nodes = set(''.join(words))
        q, res = [], ""
        for node in nodes:
            if indegree[node] == 0:
                q.append(node)
                res += node
        while q:
            node = q.pop(0)
            for end in graph[node]:
                indegree[end] -= 1
                if indegree[end] == 0:
                    q.append(end)
                    res += end
        if len(res) != len(nodes):
            return ""
        return res