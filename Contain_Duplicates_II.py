class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = i
            else:
                if i - map[nums[i]] <= k:
                    return True
                map[nums[i]] = i
        return False
