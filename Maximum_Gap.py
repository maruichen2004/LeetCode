class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        max_n, min_n = max(nums), min(nums)
        max_g = (max_n - min_n) / (len(nums)-1)
        b_size = max_g + 1
        buckets = [[] for i in range((max_n - min_n)/b_size + 1)]
        for num in nums:
            buckets[(num-min_n)/b_size].append(num)
        buckets = [b for b in buckets if b]
        for i in range(1, len(buckets)):
            max_g = max(max_g, min(buckets[i]) - max(buckets[i-1]))
        return max_g