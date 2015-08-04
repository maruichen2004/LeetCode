# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        prev, fast = None, head
        while fast and fast.next:
            fast = fast.next.next
            head.next, prev, head = prev, head, head.next
        tail = head.next if fast else head
        res = True
        while prev:
            res = res and prev.val == tail.val
            prev.next, head, prev = head, prev, prev.next
            tail = tail.next
        return res