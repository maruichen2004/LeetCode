# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.len = 0
        cur = head
        while cur:
            self.len += 1
            cur = cur.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        tmp = random.randint(0, self.len-1)
        cur = self.head
        while tmp:
            cur = cur.next
            tmp -= 1
        return cur.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()