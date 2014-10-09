# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        while cur and cur.next:
            if cur.val > cur.next.val:
                prev = dummy
                while prev.next.val < cur.next.val: prev = prev.next
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = prev.next
                prev.next =tmp
            else:
                cur = cur.next
        return dummy.next
