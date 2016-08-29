class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return self.dfs(pattern, str, {})
        
    def dfs(self, pattern, str, map):
        if len(pattern) == 0 and len(str) > 0:
            return False
        if len(pattern) == 0 and len(str) == 0:
            return True
        for end in range(1, len(str)-len(pattern)+2):
            if pattern[0] in map and map[pattern[0]] == str[:end]:
                if self.dfs(pattern[1:], str[end:], map):
                    return True
            elif pattern[0] not in map and str[:end] not in map.values():
                map[pattern[0]] = str[:end]
                if self.dfs(pattern[1:], str[end:], map):
                    return True
                del map[pattern[0]]
        return False