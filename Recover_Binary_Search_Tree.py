# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        nodes, vals = [], []
        self.inorder(root, nodes, vals)
        vals.sort()
        for i, node in enumerate(nodes):
            node.val = vals[i]
        
    def inorder(self, root, nodes, vals):
        if root is not None:
            self.inorder(root.left, nodes, vals)
            nodes.append(root)
            vals.append(root.val)
            self.inorder(root.right, nodes, vals)