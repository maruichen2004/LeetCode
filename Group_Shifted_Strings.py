class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        res = []
        map = {}
        for string in strings:
            key = ""
            for c in string:
                key += str((ord(c) - ord(string[0]) + 26) % 26) + ','
            if key not in map:
                map[key] = []
            map[key].append(string)
        for key in map:
            res.append(sorted(map[key]))
        return res