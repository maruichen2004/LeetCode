# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        dummy = ListNode(0)
        cur, map = dummy, {}
        while head:
            copy = RandomListNode(head.label)
            cur.next = copy
            map[head] = copy
            cur, head = cur.next, head.next
        for node in map:
            if node.random:
                map[node].random = map[node.random]
        return dummy.next
