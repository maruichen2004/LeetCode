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
        nodes = [None, None, None]
        self.recoverTreeHelper(root, nodes)
        nodes[0].val, nodes[1].val = nodes[1].val, nodes[0].val
        return root
        
    def recoverTreeHelper(self, root, nodes):
        if root is None: return
        self.recoverTreeHelper(root.left, nodes)
        if nodes[2] and nodes[2].val > root.val:
            nodes[1] = root
            if nodes[0] is None: nodes[0] = nodes[2]
        nodes[2] = root
        self.recoverTreeHelper(root.right, nodes)
