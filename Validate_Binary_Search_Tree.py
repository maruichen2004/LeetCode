# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        inf = 2**32 - 1
        return self.check(-inf, root, inf)
        
    def check(self, MIN, root, MAX):
        if root is None: return True
        if not MIN < root.val < MAX: return False
        return self.check(MIN, root.left, root.val) and self.check(root.val, root.right, MAX)
