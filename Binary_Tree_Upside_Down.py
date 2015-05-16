class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class Solution:
    def upsideDownBinaryTree(self, root):
        p, parent, parent_right = root, None, None
        while p:
            left = p.left
            p.left = parent_right
            parent_right = p.right
            p.right = parent
            p = left
        return parent
