class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if len(points) == 0:
            return True
        map = collections.defaultdict(set)
        min_x, max_x = float('inf'), float('-inf')
        for x, y in points:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            map[x].add(y)
        m = (min_x + max_x) * 1.0 / 2
        for x, y in points:
            t = 2 * m - x
            if t not in map or y not in map[t]:
                return False
        return True