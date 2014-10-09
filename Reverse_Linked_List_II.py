# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        diff, dummy, cur = n - m, ListNode(0), head
        dummy.next = head
        last = dummy
        while m > 1 and cur:
            last = cur
            cur = cur.next
            m -= 1
        first, prev = cur, last
        while cur and diff >= 0:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            diff -= 1
        last.next = prev
        first.next = cur
        return dummy.next
