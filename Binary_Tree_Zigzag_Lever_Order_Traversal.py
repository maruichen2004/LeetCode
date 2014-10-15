# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if root is None: return []
        res, cur, reverse = [], [root], 0
        while cur:
            next, vals = [], []
            for node in cur:
                if reverse == 0: vals.append(node.val)
                else: vals.insert(0, node.val)
                if node.left: next.append(node.left)
                if node.right: next.append(node.right)
            res.append(vals)
            reverse = 1 - reverse
            cur = next
        return res
