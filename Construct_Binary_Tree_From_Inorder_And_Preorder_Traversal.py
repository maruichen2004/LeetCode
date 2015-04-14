# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder: return None
        rootVal = preorder.pop(0)
        root = TreeNode(rootVal)
        idx = inorder.index(rootVal)
        root.left = self.buildTree(preorder, inorder[:idx])
        root.right = self.buildTree(preorder, inorder[idx+1:])
	return root
