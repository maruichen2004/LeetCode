# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        return self.check(root) != -1
        
    def check(self, root):
        if root is None: return 0
        left = self.check(root.left)
        right = self.check(root.right)
        if left < 0 or right < 0 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
