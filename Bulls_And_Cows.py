class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        cows, bulls, s_map, g_map = 0, 0, [0] * 10, [0] * 10
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                cows += 1
            else:
                s_map[int(secret[i])] += 1
                g_map[int(guess[i])] += 1
        for i in range(10):
            bulls += min(s_map[i], g_map[i])
        return str(cows) + 'A' + str(bulls) + 'B'