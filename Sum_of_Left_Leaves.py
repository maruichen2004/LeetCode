# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, None)
    
    def dfs(self, root, parent):
        if root is None:
            return 0
        if root.left is None and root.right is None and (parent is not None and root == parent.left):
            return root.val
        return self.dfs(root.left, root) + self.dfs(root.right, root)