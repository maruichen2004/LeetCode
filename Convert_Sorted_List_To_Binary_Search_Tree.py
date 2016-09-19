# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)
        slow, fast, last = head, head, head
        while fast.next and fast.next.next:
            last = slow
            slow = slow.next
            fast = fast.next.next
        fast = slow.next
        last.next = None
        root = TreeNode(slow.val)
        if head != slow:
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(fast)
        return root