class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = [0] * (len(nums) + 1)
        self.bit = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.update(i, nums[i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        diff = val - self.nums[i+1]
        j = i + 1
        while j < len(self.nums):
            self.bit[j] += diff
            j += (j & -j)
        self.nums[i+1] = val

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.getSum(j+1) - self.getSum(i)

    def getSum(self, i):
        res = 0
        j = i
        while j > 0:
            res += self.bit[j]
            j -= (j & -j)
        return res

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)