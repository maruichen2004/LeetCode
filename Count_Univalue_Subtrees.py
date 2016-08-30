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
        return self.helper(root, True)[1]
        
    def helper(self, root, isUni):
        if root is None:
            return True, 0
        left, left_val = self.helper(root.left, True)
        right, right_val = self.helper(root.right, True)
        uni = left and right and (root.val == root.left.val if root.left else True) and (root.val == root.right.val if root.right else True)
        return uni, left_val + right_val + uni