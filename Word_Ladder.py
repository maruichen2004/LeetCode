class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        dict.add(end)
        queue = collections.deque([(start, 1)])
        while queue:
            cur = queue.popleft()
            curword, curlen = cur[0], cur[1]
            if curword == end: return curlen
            for i in range(len(curword)):
                for j in "abcdefghijklmnopqrstuvwxyz":
                    if curword[i] != j:
                        nextword = curword[:i] + j + curword[i+1:]
                        if nextword in dict:
                            queue.append((nextword, curlen + 1))
                            dict.remove(nextword)
        return 0
