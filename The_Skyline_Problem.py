class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        """
        For each iteration, we first find the current process time, which is either the next new building start time or the end time of the top entry of the live queue. If the new building start time is larger than the top one end time, then process the one in the queue first (pop them until it is empty or find the first one that ends after the new building); otherswise, if the new building starts before the top one ends, then process the new building (just put them in the queue). After processing, output it to the resulting vector if the height changes. Complexity is the worst case O(NlogN)
        """
        skyline = []
        i, n = 0, len(buildings)
        # first: height, second, end time
        heap = []
        #if either some new building is not processed or live building queue is not empty
        while i < n or heap:
            #the next new building starts before the top one ends, process the new building in the vector
            if len(heap) == 0 or i < n and buildings[i][0] <= heap[0][1]:
                #next timing point to process
                x = buildings[i][0]
                #go through all the new buildings that starts at the same point
                while i < n and buildings[i][0] == x:
                    #just push them in the queue
                    heapq.heappush(heap, (-buildings[i][2], buildings[i][1]))
                    i += 1
            #the current tallest building will end before the next timing point
            else:
                #next timing point to process
                x = heap[0][1]
                #pop up the processed buildings, i.e. those  have height no larger than cur_H and end before the top one
                while heap and heap[0][1] <= x:
                    heapq.heappop(heap)
            #outut the top one
            height = len(heap) and -heap[0][0]
            if not skyline or height != skyline[-1][1]:
                skyline += [x, height],
        return skyline