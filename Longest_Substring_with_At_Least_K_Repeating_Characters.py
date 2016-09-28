class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res, i, n = 0, 0, len(s)
        while i + k < n:
            m, mask, mx_id = [0] * 26, 0, i
            for j in range(i, n):
                t = ord(s[j]) - ord('a')
                m[t] += 1
                if m[t] < k:
                    mask |= (1 << t)
                else:
                    mask &= (~(1 << t))
                if mask == 0:
                    res = max(res, j - i + 1)
                    mx_id = j
            i = mx_id + 1
        return res