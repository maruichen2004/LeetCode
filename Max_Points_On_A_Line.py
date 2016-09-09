# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        d = collections.defaultdict(list)
        for p, q in itertools.combinations(points, 2):
            if p.x == q.x:
                t = (float('inf'), p.x)
            else:
                t = ((p.y-q.y)/float((p.x-q.x)), (p.x*q.y-q.x*p.y)/float(p.x-q.x))
            d[t] += [p, q]
        return max(len(set(l)) for l in d.values()) if len(points) > 1 else len(points)