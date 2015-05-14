class MinStack:
    def __init__(self):
        self.stack = []
        
    # @param x, an integer
    # @return an integer
    def push(self, x):
        if len(self.stack) == 0: self.stack.append((x, x))
        else: self.stack.append((x, min(x, self.stack[-1][1])))

    # @return nothing
    def pop(self):
        if len(self.stack) == 0: return
        else:
            self.stack.pop()

    # @return an integer
    def top(self):
        if len(self.stack) == 0: return -1
        else: return self.stack[-1][0]

    # @return an integer
    def getMin(self):
        if len(self.stack) == 0: return -1
        else: return self.stack[-1][1]
