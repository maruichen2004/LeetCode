class Solution:
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None: return None
        cur, lenA = headA, 1
        while cur.next:
            cur, lenA = cur.next, lenA + 1
        cur, lenB = headB, 1
        while cur.next:
            cur, lenB = cur.next, lenB + 1
        l1, l2 = headA, headB
        if lenB < lenA: l1, l2 = l2, l1
        for i in range(abs(lenA - lenB)): l2 = l2.next
        while l1 and l2:
            if l1 == l2: return l1
            l1, l2 = l1.next, l2.next
        return None
