# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        cur = root
        prev, next, tmp = None, None, None
        while cur:
            next = cur.left
            cur.left = tmp
            tmp = cur.right
            cur.right = prev
            prev = cur
            cur = next
        return prev