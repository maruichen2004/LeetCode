class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        flag = False
        for pair in zip(words, words[1:]):
            if len(pair[1]) < len(pair[0]):
                flag = True
            for a, b in zip(*pair):
                if a != b:
                    graph[a].append(b)
                    indegree[b] += 1
                    break
        if not indegree and flag:
            return ""
        nodes = set(''.join(words))
        res, q = "", []
        for node in nodes:
            if indegree[node] == 0:
                res += node
                q.append(node)
        while q:
            node = q.pop(0)
            for end in graph[node]:
                if end in indegree:
                    indegree[end] -= 1
                    if indegree[end] == 0:
                        res += end
                        q.append(end)
        if len(res) != len(nodes):
            return ""
        return res