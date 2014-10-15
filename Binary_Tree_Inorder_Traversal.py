# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
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
                    prev.right = cur
                    cur = cur.left
                else:
                    prev.right = None
                    res.append(cur.val)
                    cur = cur.right
        return res
        '''
        def inorderTraversal(self, root):
            if root is None: return []
            res, stack, cur = [], [], root
            while stack or cur:
                if cur:
                    stack.append(cur)
                    cur = cur.left
                else:
                    parent = stack.pop()
                    res.append(parent.val)
                    cur = parent.right
            return res
            '''
