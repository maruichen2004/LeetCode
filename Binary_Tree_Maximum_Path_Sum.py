# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)[1]
        
    def helper(self, root):
        if root is None:
            return 0, -sys.maxint
        left = self.helper(root.left)
        right = self.helper(root.right)
        singlePath = max(left[0] + root.val, right[0] + root.val, 0)
        maxPath = max(left[1], right[1], left[0] + right[0] + root.val)
        return singlePath, maxPath