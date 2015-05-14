class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    # @return an integer
    def get(self, key):
        if key not in self.cache: return -1
        val = self.cache[key]
        del self.cache[key]
        self.cache[key] = val
        return val

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache:
            del self.cache[key]
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value
