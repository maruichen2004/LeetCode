class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.s1 = []
        self.s2 = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.s1.append(x)

    # @return nothing
    def pop(self):
        self.peek()
        self.s2.pop()

    # @return an integer
    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    # @return an boolean
    def empty(self):
        return not self.s1 and not self.s2
