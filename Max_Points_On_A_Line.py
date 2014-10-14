# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        res = 0
        for i in range(len(points)):
            slopemap, same, inf, curmax = {}, 1, 0, 0
            start = points[i]
            for j in range(i + 1, len(points)):
                end = points[j]
                if start.x == end.x and start.y == end.y:
                    same += 1
                elif start.x == end.x:
                    inf += 1
                else:
                    slope = 1.0 * (start.y - end.y) / (start.x - end.x)
                    if slope not in slopemap:
                        slopemap[slope] = 1
                    else:
                        slopemap[slope] += 1
            for slope in slopemap:
                curmax = max(curmax, same + slopemap[slope])
            res = max(res, same + inf, curmax)
        return res
