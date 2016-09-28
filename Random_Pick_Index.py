class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = list(nums)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        cnt = 0
        res = 0
        for i, num in enumerate(self.nums):
            if num == target:
                cnt += 1
                t = random.randint(0, cnt-1)
                if t  == 0:
                    res = i
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)