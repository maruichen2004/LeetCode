# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        res = []
        if root is not None:
            self.helper(res, str(root.val), root)
        return res
    
    def helper(self, res, cur, root):
        if root.left is None and root.right is None:
            res.append(cur)
            return
        if root.left:
            self.helper(res, cur + "->" + str(root.left.val), root.left)
        if root.right:
            self.helper(res, cur + "->" + str(root.right.val), root.right)
