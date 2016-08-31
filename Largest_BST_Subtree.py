# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root)[2]
        
    def dfs(self, root):
        if root is None:
            return True, (float('inf'), float('-inf')), 0
        left_bst, left_range, left_cnt = self.dfs(root.left)
        right_bst, right_range, right_cnt = self.dfs(root.right)
        if left_bst and right_bst and left_range[1] < root.val < right_range[0]:
            return True, (min(left_range[0], root.val), max(root.val, right_range[1])), left_cnt + right_cnt + 1
        return False, None, max(left_cnt, right_cnt)