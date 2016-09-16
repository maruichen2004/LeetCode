# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root)[1]
        
    def dfs(self, root):
        if root is None:
            return True, 0
        left, left_val = self.dfs(root.left)
        right, right_val = self.dfs(root.right)
        uni = left and right and (root.left.val == root.val if root.left else True) and (root.right.val == root.val if root.right else True)
        return uni, left_val + right_val + uni