class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need, missing = collections.Counter(t), len(t)
        start, min_start, min_end = 0, 0, 0
        for end, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if missing == 0:
                while start < end and need[s[start]] < 0:
                    need[s[start]] += 1
                    start += 1
                if min_end == 0 or end - start < min_end - min_start:
                    min_start, min_end = start, end
        return s[min_start:min_end]