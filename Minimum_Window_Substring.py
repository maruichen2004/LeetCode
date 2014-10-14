ass Solution:
    # @return a string
    def minWindow(self, S, T):
        map = {}
        for char in T:
            if char not in map: map[char] = 1
            else: map[char] += 1
        count = len(T)
        start, minstart, minsize = 0, 0, len(S) + 1
        for end in range(len(S)):
            if S[end] in map:
                map[S[end]] -= 1
                if map[S[end]] >= 0: count -= 1
            if count == 0:
                while True:
                    if S[start] in map:
                        if map[S[start]] < 0: map[S[start]] += 1
                        else: break
                    start += 1
                if end - start + 1 < minsize:
                    minsize = end - start + 1
                    minstart = start
        if minsize == len(S) + 1: return ""
        return S[minstart:minstart+minsize]
