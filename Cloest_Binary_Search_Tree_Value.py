# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        cur, cloest, res = root, sys.maxint, 0
        while cur:
            if cur.val == target:
                return cur.val
            if abs(cur.val - target) < abs(cloest):
                cloest = cur.val - target
                res = cur.val
            if cur.val < target:
                cur = cur.right
            else:
                cur = cur.left
        return res