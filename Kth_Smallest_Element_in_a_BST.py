# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        stack, cur, rank = [], root, 0
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            parent = stack.pop()
            rank += 1
            if rank == k:
                return parent.val
            cur = parent.right
        return float("-inf")
