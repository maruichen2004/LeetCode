# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l + 1 < r:
            mid = (l + r) / 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                l = mid
            else:
                r = mid
        if guess(l) == 0:
            return l
        if guess(r) == 0:
            return r
        return -1
