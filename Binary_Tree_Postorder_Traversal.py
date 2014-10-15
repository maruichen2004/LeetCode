# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if root is None: return []
        res, stackPrep, stackRdy = [], [root], []
        while stackPrep:
            cur = stackPrep.pop()
            stackRdy.append(cur.val)
            if cur.left: stackPrep.append(cur.left)
            if cur.right: stackPrep.append(cur.right)
        while stackRdy:
            res.append(stackRdy.pop())
        return res
