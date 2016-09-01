class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res, map = [], collections.defaultdict(int)
        for c in s:
            map[c] += 1
        t, mid = "", ""
        for key in map:
            if map[key] % 2 == 1:
                mid += key
            map[key] /= 2
            t += key * map[key]
            if len(mid) > 1:
                return []
        self.helper(t, map, mid, "", res)
        return res
        
    def helper(self, t, map, mid, cur, res):
        if len(cur) >= len(t):
            res.append(cur + mid + cur[::-1])
        else:
            for key in map:
                if map[key] > 0:
                    map[key] -= 1
                    self.helper(t, map, mid, cur+key, res)
                    map[key] += 1