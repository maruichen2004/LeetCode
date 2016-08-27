class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest, start, map = 0, 0, {}
        for i, c in enumerate(s):
            if c not in map:
                map[c] = 0
            map[c] += 1
            while len(map) > 2:
                map[s[start]] -= 1
                if map[s[start]] == 0:
                    del map[s[start]]
                start += 1
            longest = max(longest, i - start + 1)
        return longest