# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if head is None or head.next is None: return head
        dummy = ListNode(0)
        dummy.next, prev = head, dummy
        while True:
            begin, end = prev.next, prev
            for i in range(k):
                end = end.next
                if end is None: return dummy.next
            newStart = end.next
            self.reverse(begin, end)
            begin.next = newStart
            prev.next = end
            prev = begin
    
    def reverse(self, start, end):
        cur, prev = start, start
        next = cur.next
        while cur != end:
            cur = next
            next = next.next
            cur.next = prev
            prev = cur
