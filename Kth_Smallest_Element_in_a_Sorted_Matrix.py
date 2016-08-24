class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []
        for i in range(min(k, len(matrix))):
            heap.append((matrix[i][0], i, 0))
        heapq.heapify(heap)
        for i in range(k-1):
            _, x, y = heapq.heappop(heap)
            if y + 1 < len(matrix[x]):
                heapq.heappush(heap, (matrix[x][y+1], x, y+1))
        return heap[0][0]