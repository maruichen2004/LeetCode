class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        if not word or not abbr:
            return False
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i, j = i + 1, j + 1
                continue
            if not abbr[j].isdigit():
                return False
            start = j
            while j < len(abbr) and abbr[j].isdigit():
                j += 1
            num = int(abbr[start:j])
            if num == 0 or str(num) != abbr[start:j]:
                return False
            i += num
        return i == len(word) and j == len(abbr)