class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class Solution:
    def upsideDownBinaryTree(self, root):
        tmp, newRoot = None, [None]
        tmp = self.upsideDownBinaryTreeHelper(root, newRoot)
        return newRoot[0]
    
    def upsideDownBinaryTreeHelper(self, root, newRoot):
        if root is None: return None
        if root.left is None and root.right is None:
            newRoot[0] = root
            return root
        parent = self.upsideDownBinaryTreeHelper(root.left, newRoot)
        parent.left = root.right
        parent.right = root
        root.left = None
        root.right = None
        return parent.right
