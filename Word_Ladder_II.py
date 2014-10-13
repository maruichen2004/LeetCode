class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        res, trace, cur = [], {word:[] for word in dict}, set([start])
        while cur and end not in cur:
            for word in cur: dict.remove(word)
            next = set()
            for word in cur:
                for i in range(len(word)):
                    for j in "abcdefghijklmnopqrstuvwxyz":
                        if word[i] != j:
                            nextword = word[:i] + j + word[i+1:]
                            if nextword in dict:
                                next.add(nextword)
                                trace[nextword].append(word)
            cur = next
        if cur: self.backtrack(res, [], trace, end)
        return res
        
    def backtrack(self, res, path, trace, word):
        if len(trace[word]) == 0: res.append([word] + path)
        else:
            for prev in trace[word]:
                self.backtrack(res, [word] + path, trace, prev)
