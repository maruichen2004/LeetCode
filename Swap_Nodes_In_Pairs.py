# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None or head.next is None: return head
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            n1, n2 = cur.next, cur.next.next
            cur.next = n2
            n1.next = n2.next
            n2.next = n1
            cur = n1
        return dummy.next
