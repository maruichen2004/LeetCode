# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if len(num) == 0: return None
        return self.sortedArrayToBSTRec(num, 0, len(num) - 1)
        
    def sortedArrayToBSTRec(self, num, l, r):
        if l > r: return None
        mid = (l + r) / 2
        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBSTRec(num, l, mid - 1)
        root.right = self.sortedArrayToBSTRec(num, mid + 1, r)
        return root
