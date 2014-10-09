# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head is None or head.next is None: return head
        cur, length = head, 1
        while cur.next != None:
            cur, length = cur.next, length + 1
        dummy = ListNode(0)
        dummy.next, interval = head, 1
        while interval <= length:
            prev, slow, fast = dummy, dummy.next, dummy.next
            while fast or slow:
                i = 0
                while i < interval and fast:
                    fast, i = fast.next, i + 1
                    fvisit, svisit = 0, 0
                while fvisit < interval and svisit < interval and fast and slow:
                    if fast.val < slow.val:
                        prev.next, prev, fast, fvisit = fast, fast, fast.next, fvisit + 1
                    else:
                        prev.next, prev, slow, svisit = slow, slow, slow.next, svisit + 1
                while fvisit < interval and fast:
                    prev.next, prev, fast, fvisit = fast, fast, fast.next, fvisit + 1
                while svisit < interval and slow:
                    prev.next, prev, slow, svisit = slow, slow, slow.next, svisit + 1
                prev.next, slow = fast, fast
            interval *= 2
        return dummy.next
