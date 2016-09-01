class Solution(object):
    def rearrangeString(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        if k == 0:
            return str
        map, res = collections.defaultdict(int), []
        for c in str:
            map[c] += 1
        heap = []
        length = len(str)
        for key, val in map.items():
            heapq.heappush(heap, (-val, key))
        while heap:
            tmp = []
            cnt = min(k, length)
            for i in range(cnt):
                if not heap:
                    return ""
                v, c = heapq.heappop(heap)
                res.append(c)
                v = -v - 1
                if v > 0:
                    tmp.append((-v, c))
                length -= 1
            for item in tmp:
                heapq.heappush(heap, item)
        return ''.join(res)