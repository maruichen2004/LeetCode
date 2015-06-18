# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if root is None: return 0
        leftHeight, rightHeight = self.getHeight(root.left), self.getHeight(root.right)
        if leftHeight == rightHeight:
            return 2 ** (leftHeight) + self.countNodes(root.right)
        else:
            return 2 ** (leftHeight - 1) + self.countNodes(root.left)
            
    def getHeight(self, root):
        h = 0
        while root:
            root = root.left
            h += 1
        return h
