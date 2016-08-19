class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l = len(citations)
        count = [0] * (l + 1)
        for c in citations:
            count[min(l, c)] += 1
        total = 0
        for i in reversed(range(l+1)):
            total += count[i]
            if total >= i:
                return i
        return 0