class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.dict = {}

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        if number not in self.dict:
            self.dict[number] = 0
        self.dict[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for key in self.dict:
            if value - key == key:
                if self.dict[key] >= 2:
                    return True
            elif value - key in self.dict:
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)