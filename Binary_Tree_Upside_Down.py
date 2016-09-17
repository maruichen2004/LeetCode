# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None or root.left is None:
            return root
        left, right = root.left, root.right
        res = self.upsideDownBinaryTree(left)
        left.left = right
        left.right = root
        root.left = None
        root.right = None
        return res