# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        return self.sumNumbersRec(0, root)
    
    def sumNumbersRec(self, res, root):
        if root is None: return 0
        if root.left is None and root.right is None: return res * 10 + root.val
        return self.sumNumbersRec(res * 10 + root.val, root.left) + self.sumNumbersRec(res * 10 + root.val, root.right)
