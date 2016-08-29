# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        carry = self.helper(head)
        if carry == 1:
            newHead = ListNode(1)
            newHead.next = head
            return newHead
        return head
        
    def helper(self, node):
        if node is None:
            return 1
        carry = self.helper(node.next)
        sum = node.val + carry
        node.val = sum % 10
        return sum / 10