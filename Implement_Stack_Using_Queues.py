class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.q = collections.deque()

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.q.append(x)
        for i in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    # @return nothing
    def pop(self):
        self.q.popleft()

    # @return an integer
    def top(self):
        return self.q[0]

    # @return an boolean
    def empty(self):
        return len(self.q) == 0
