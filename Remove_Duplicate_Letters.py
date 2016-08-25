class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        map, visited = [0] * 256, [0] * 256
        res = ['0']
        for c in s:
            map[ord(c)] += 1
        for i in range(len(s)):
            map[ord(s[i])] -= 1
            if visited[ord(s[i])]:
                continue
            while ord(s[i]) < ord(res[-1]) and map[ord(res[-1])]:
                visited[ord(res.pop())] = 0
            res.append(s[i])
            visited[ord(s[i])] = 1
        return ''.join(res)[1:]