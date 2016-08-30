class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        queue = []
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        while queue:
            i, j = queue.pop(0)
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if x < 0 or x > len(rooms)-1 or y < 0 or y > len(rooms[0])-1 or rooms[x][y] < rooms[i][j] + 1:
                    continue
                rooms[x][y] = rooms[i][j] + 1
                queue.append((x, y))