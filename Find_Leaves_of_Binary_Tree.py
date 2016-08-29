# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        while root:
            leaves = []
            root = self.helper(root, leaves)
            res.append(leaves)
        return res
        
    def helper(self, root, leaves):
        if root is None:
            return None
        if root.left is None and root.right is None:
            leaves.append(root.val)
            return None
        root.left = self.helper(root.left, leaves)
        root.right = self.helper(root.right, leaves)
        return root