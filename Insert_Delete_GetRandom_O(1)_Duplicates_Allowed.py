class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = collections.defaultdict(set)
        self.lst = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        contain = val not in self.map
        self.lst.append(val)
        self.map[val].add(len(self.lst) - 1)
        return contain

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.map:
            return False
        idx = self.map[val].pop()
        last = self.lst[-1]
        if len(self.map[val]) == 0:
            del self.map[val]
        self.lst[idx] = last
        if last in self.map:
            self.map[last].add(idx)
            self.map[last].discard(len(self.lst)-1)
        self.lst.pop()
        return True
        
    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        idx = random.randint(0, len(self.lst) - 1)
        return self.lst[idx]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()