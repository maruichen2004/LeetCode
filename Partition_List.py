# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        smaller_head, larger_head = ListNode(0), ListNode(0)
        smaller, larger, cur = smaller_head, larger_head, head
        while cur:
            if cur.val < x:
                smaller.next = cur
                smaller = smaller.next
            else:
                larger.next = cur
                larger = larger.next
            cur = cur.next
        smaller.next = larger_head.next
        larger.next = None
        return smaller_head.next
