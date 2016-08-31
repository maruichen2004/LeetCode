# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        map = collections.defaultdict(list)
        queue = [(0, root)]
        res = []
        while queue:
            col, node = queue.pop(0)
            map[col].append(node.val)
            if node.left:
                queue.append((col-1, node.left))
            if node.right:
                queue.append((col+1, node.right))
        for k in sorted(map.keys()):
            res.append(map[k])
        return res