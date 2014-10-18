# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        self.maxsum = -2**32 + 1
        self.maxPathSumRec(root)
        return self.maxsum
        
    def maxPathSumRec(self, root):
        if root is None: return 0
        left = max(0, self.maxPathSumRec(root.left))
        right = max(0, self.maxPathSumRec(root.right))
        self.maxsum = max(self.maxsum, root.val + left + right)
        return root.val + max(left, right)
