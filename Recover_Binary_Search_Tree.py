# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        self.prev, self.n1, self.n2 = None, None, None
        self.inorder(root)
        self.n1.val, self.n2.val = self.n2.val, self.n1.val
        return root
        
    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            if self.prev is None: self.prev = root
            if self.n1 is None and self.prev.val > root.val:
                self.n1 = self.prev
                self.n2 = root
            elif self.prev.val > root.val:
                self.n2 = root
            self.prev = root
            self.inorder(root.right)
