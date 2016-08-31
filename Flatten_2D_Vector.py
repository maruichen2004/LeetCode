class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.v = vec2d
        self.x = 0
        self.y = 0

    def next(self):
        """
        :rtype: int
        """
        self.y += 1
        return self.v[self.x][self.y-1]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.x < len(self.v) and self.y == len(self.v[self.x]):
            self.x += 1
            self.y = 0
        return self.x < len(self.v)

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())