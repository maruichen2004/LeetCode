# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        odd_head, even_head = ListNode(0), ListNode(0)
        odd, even = odd_head, even_head
        cur = head
        while cur:
            if cur:
                odd.next = cur
                cur = cur.next
                odd = odd.next
            if cur:
                even.next = cur
                cur = cur.next
                even = even.next
        odd.next = even_head.next
        even.next = None
        return odd_head.next
        