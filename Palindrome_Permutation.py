class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        odd_cnt = 0
        map = collections.defaultdict(int)
        for c in s:
            map[c] += 1
        for key, val in map.items():
            if val % 2 == 1:
                odd_cnt += 1
        if odd_cnt > 1:
            return False
        return True