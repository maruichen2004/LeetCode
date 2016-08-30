# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, None, 0)
        
    def dfs(self, root, parent, res):
        if root is None:
            return res
        if parent and root.val == parent.val + 1:
            res += 1
        else:
            res = 1
        left = self.dfs(root.left, root, res)
        right = self.dfs(root.right, root, res)
        return max(res, left, right)