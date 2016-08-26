class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if len(envelopes) == 0:
            return 0
        dp = []
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        for i in range(len(envelopes)):
            l, r = 0, len(dp)
            while l < r:
                mid = (l + r) / 2
                if dp[mid] < envelopes[i][1]:
                    l = mid + 1
                else:
                    r = mid
            if r >= len(dp):
                dp.append(envelopes[i][1])
            else:
                dp[r] = envelopes[i][1]
        return len(dp)