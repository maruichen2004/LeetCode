# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        res = []
        cur = root
        while cur:
            if cur.left is None:
                res.append(cur.val)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right is not None and prev.right is not cur:
                    prev = prev.right
                if prev.right is None:
                    res.append(cur.val)
                    prev.right = cur
                    cur = cur.left
                else:
                    prev.right = None
                    cur = cur.right
        return res
        '''
        def preorderTraversal(self, root):
        if root is None: return []
        res, stack = [], [root]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right: stack.append(cur.right)
            if cur.left: stack.append(cur.left)
        return res
        '''
