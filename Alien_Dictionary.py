class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        edges = []
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    edges.append(a+b)
                    break
        chars = set(''.join(words))
        indegree = [0] * 26
        for e in edges:
            indegree[ord(e[1]) - ord('a')] += 1
        order = ""
        queue = []
        for c in chars:
            if indegree[ord(c) - ord('a')] == 0:
                queue.append(c)
                order += c
        while queue:
            c = queue.pop(0)
            for edge in edges:
                if edge[0] == c:
                    indegree[ord(edge[1]) - ord('a')] -= 1
                    if indegree[ord(edge[1]) - ord('a')] == 0:
                        queue.append(edge[1])
                        order += edge[1]
        if len(order) != len(chars):
            return ""
        return order