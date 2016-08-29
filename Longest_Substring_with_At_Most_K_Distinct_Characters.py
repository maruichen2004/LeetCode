class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res, left, map = 0, 0, collections.defaultdict(int)
        for right in range(len(s)):
            map[s[right]] += 1
            while len(map) > k:
                map[s[left]] -= 1
                if map[s[left]] == 0:
                    del map[s[left]]
                left += 1
            res = max(res, right - left + 1)
        return res