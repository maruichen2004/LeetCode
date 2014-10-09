# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next:
            next = cur.next
            while next.next and next.val == next.next.val:
                next = next.next
            if next != cur.next:
                cur.next = next.next
            else:
                cur = cur.next
        return dummy.next
