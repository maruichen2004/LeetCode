class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for i, j in itertools.combinations(range(1, n), 2):
            n1, n2 = num[:i], num[i:j]
            if n1 != str(int(n1)) or n2 != str(int(n2)):
                continue
            while j < n:
                n3 = str(int(n1) + int(n2))
                if not num.startswith(n3, j):
                    break
                j += len(n3)
                n1, n2 = n2, n3
            if j == n:
                return True
        return False