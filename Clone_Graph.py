# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None: return None
        start = UndirectedGraphNode(node.label)
        queue, map = [node], {node:start}
        while queue:
            next = []
            for x in queue:
                for neighbor in x.neighbors:
                    if neighbor not in map:
                        copy = UndirectedGraphNode(neighbor.label)
                        next.append(neighbor)
                        map[neighbor] = copy
                        map[x].neighbors.append(copy)
                    else:
                        map[x].neighbors.append(map[neighbor])
            queue = next
        return start
