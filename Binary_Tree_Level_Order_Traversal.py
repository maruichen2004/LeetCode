# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if root is None: return []
        res, cur = [], [root]
        while cur:
            next, vals = [], []
            for node in cur:
                vals.append(node.val)
                if node.left: next.append(node.left)
                if node.right: next.append(node.right)
            res.append(vals)
            cur = next
        return res
