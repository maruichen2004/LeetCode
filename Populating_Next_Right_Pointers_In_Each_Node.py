# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None: return
        cur = [root]
        while cur:
            next = []
            for i in range(len(cur)):
                if i < len(cur) - 1:
                    cur[i].next = cur[i + 1]
                if cur[i].left: next.append(cur[i].left)
                if cur[i].right: next.append(cur[i].right)
            cur = next
