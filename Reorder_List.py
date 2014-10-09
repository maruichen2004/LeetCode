# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head is None or head.next is None: return head
        fast, slow, prev = head, head, None
        while fast and fast.next:
            fast, slow, prev = fast.next.next, slow.next, slow
        prev.next = None
        prev = None
        cur = slow
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        dummy = ListNode(0)
        cur = dummy
        while prev or head:
            if head:
                cur.next = head; cur = cur.next; head = head.next
            if prev:
                cur.next = prev; cur = cur.next; prev = prev.next
        return dummy.next
