class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map = {}
        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1
        heap = []
        for key, val in map.items():
            heap.append((-val, key))
        heapq.heapify(heap)
        res = []
        for i in range(k):
            cur = heapq.heappop(heap)
            res.append(cur[1])
        return res