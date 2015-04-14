# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder: return None
        rootVal = postorder.pop()
        root = TreeNode(rootVal)
        idx = inorder.index(root.val)
        root.right = self.buildTree(inorder[idx+1:], postorder)
        root.left = self.buildTree(inorder[:idx], postorder)
        return root
