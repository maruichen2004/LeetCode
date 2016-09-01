class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        conors = collections.defaultdict(int)
        left, right, bottom, top = float('inf'), 0, float('inf'), 0
        area = 0
        for rect in rectangles:
            left = min(left, rect[0])
            right = max(right, rect[2])
            bottom = min(bottom, rect[1])
            top = max(top, rect[3])
            area += (rect[2] - rect[0]) * (rect[3] - rect[1])
            for point in [(rect[0], rect[1]), (rect[2], rect[1]), (rect[2], rect[3]), (rect[0], rect[3])]:
                conors[point] += 1
        if area != (right - left) * (top - bottom):
            return False
        rectangle = [(left, bottom), (right, bottom), (left, top), (right, top)]
        for conor in rectangle:
            if conor not in conors or conors[conor] != 1:
                return False
        for conor in conors:
            if conor not in rectangle and conors[conor] != 2 and conors[conor] != 4:
                return False
        return True