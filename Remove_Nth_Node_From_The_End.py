# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        for i in range(n): cur = cur.next
        prev = dummy
        while cur.next:
            prev, cur = prev.next, cur.next
        prev.next = prev.next.next
        return dummy.next
