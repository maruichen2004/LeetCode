class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        n = len(nums)
        mx, mn = float('-inf'), float('inf')
        for num in nums:
            mx = max(num, mx)
            mn = min(num, mn)
        bucket_size = (mx - mn) / n + 1
        bucket_num = (mx - mn) / bucket_size + 1
        bucket_min = [float('inf')] * bucket_num
        bucket_max = [float('-inf')] * bucket_num
        bucket_used = set()
        for num in nums:
            idx = (num - mn) / bucket_size
            bucket_min[idx] = min(bucket_min[idx], num)
            bucket_max[idx] = max(bucket_max[idx], num)
            bucket_used.add(idx)
        i, res = 0, 0
        for j in range(1, bucket_num):
            if j not in bucket_used:
                continue
            res = max(res, bucket_min[j] - bucket_max[i])
            i = j
        return res