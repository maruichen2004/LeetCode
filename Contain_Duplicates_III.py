class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        map = {}
        for i, n in enumerate(nums):
            (bucket, offset) = (n/t, 1) if t != 0 else (n, 0)
            for b in range(bucket - offset, bucket + offset + 1):
                if b in map and abs(i - map[b][0]) <= k and abs(n - map[b][1]) <= t:
                    return True
            map[bucket] = (i, n)
        return False