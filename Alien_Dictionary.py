class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    graph[a].append(b)
                    indegree[b] += 1
                    break
        nodes = set(''.join(words))
        res, q = "", []
        for node in nodes:
            if indegree[node] == 0:
                res += node
                q.append(node)
        while q:
            node = q.pop(0)
            for end in graph[node]:
                indegree[end] -= 1
                if indegree[end] == 0:
                    res += end
                    q.append(end)
        if len(res) != len(nodes):
            return ""
        return res