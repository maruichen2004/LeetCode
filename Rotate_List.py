# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head is None or head.next is None: return head
        cur, length = head, 1
        while cur.next:
            cur = cur.next
            length += 1
        cur.next = head
        k = length - k % length
        for i in range(k): cur = cur.next
        newHead = cur.next
        cur.next = None
        return newHead
