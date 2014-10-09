# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        heap = []
        for node in lists:
            if node: heap.append((node.val, node))
        heapq.heapify(heap)
        dummy = ListNode(0)
        cur = dummy
        while heap:
            pop = heapq.heappop(heap)
            cur.next = pop[1]
            cur = cur.next
            if pop[1].next:
                heapq.heappush(heap, (pop[1].next.val, pop[1].next))
        return dummy.next
