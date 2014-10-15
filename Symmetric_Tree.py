# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root is None: return True
        return self.isMirrorTree(root.left, root.right)
        
    def isMirrorTree(self, p, q):
        if p is None and q is None: return True
        if p is None or q is None or p.val != q.val: return False
        return self.isMirrorTree(p.left, q.right) and self.isMirrorTree(p.right, q.left)
