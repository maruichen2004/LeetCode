class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = set()
        res, left, right = 0, 0, 0
        while right < len(s):
            if s[right] not in t:
                t.add(s[right])
                right += 1
                res = max(res, len(t))
            else:
                t.discard(s[left])
                left += 1
        return res