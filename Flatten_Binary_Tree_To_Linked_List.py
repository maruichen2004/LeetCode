# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root is None: return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left is None: return
        cur = root.left
        while cur.right: cur = cur.right
        cur.right = root.right
        root.right = root.left
        root.left = None
