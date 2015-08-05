class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
        q = collections.deque()
        res = []
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        for i in range(k, len(nums)):
            res.append(nums[q[0]])
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            while q and q[0] <= i - k:
                q.popleft()
            q.append(i)
        if q:
            res.append(nums[q[0]])
        return res
