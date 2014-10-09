# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 or l2:
            sum = carry
            if l1: 
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            carry = sum / 10
            sum %= 10
            cur.next = ListNode(sum)
            cur = cur.next
        if carry != 0: cur.next = ListNode(carry)
        return dummy.next
