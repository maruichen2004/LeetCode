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
        if len(points) <= 1:
            return len(points)
        d = collections.defaultdict(set)
        for p, q in itertools.combinations(points, 2):
            if p.x == q.x:
                t = (float('inf'), p.x)
            else:
                t = ((p.y-q.y)/float((p.x-q.x)), (p.x*q.y - q.x*p.y)/float((p.x-q.x)))
            d[t].add(p)
            d[t].add(q)
        return max(len(l) for l in d.values())