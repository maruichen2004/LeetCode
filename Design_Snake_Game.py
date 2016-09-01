class SnakeGame(object):

    def __init__(self, width,height,food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.width = width
        self.height = height
        self.pos = [[0, 0]]
        self.food = [list(f) for f in food]
        self.score = 0

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        head = list(self.pos[0])
        tail = self.pos.pop()
        if direction == 'U':
            head[0] -= 1
        elif direction == 'D':
            head[0] += 1
        elif direction == 'L':
            head[1] -= 1
        elif direction == 'R':
            head[1] += 1
        if not 0 <= head[0] < self.height or not 0 <= head[1] < self.width or head in self.pos:
            return -1
        self.pos.insert(0, head)
        if len(self.food) > 0 and head == self.food[0]:
            self.food.pop(0)
            self.pos.append(tail)
            self.score += 1
        return self.score
# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)