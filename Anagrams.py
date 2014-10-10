class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        map, res = {}, []
        for word in strs:
            sortedword = "".join(sorted(word))
            if sortedword not in map: map[sortedword] = [word]
            else: map[sortedword] += [word]
        for item in map:
            if len(map[item]) > 1: res += map[item]
        return res
