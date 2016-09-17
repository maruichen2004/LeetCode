# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left, left_height, right, right_height = root, 0, root, 0
        while left:
            left_height += 1
            left = left.left
        while right:
            right_height += 1
            right = right.right
        if left_height == right_height:
            return 2 ** left_height - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1