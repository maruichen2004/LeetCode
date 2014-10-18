# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        cur, length = head, 0
        while cur:
            cur, length = cur.next, length + 1
        self.head = head
        return self.sortedListToBSTRec(0, length - 1)
        
    def sortedListToBSTRec(self, l, r):
        if l > r: return None
        mid = (l + r) / 2
        left = self.sortedListToBSTRec(l, mid - 1)
        root = TreeNode(self.head.val)
        root.left = left
        self.head = self.head.next
        root.right = self.sortedListToBSTRec(mid + 1, r)
        return root
