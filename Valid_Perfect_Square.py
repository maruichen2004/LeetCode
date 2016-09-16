class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l, r = 0, num
        while l + 1 < r:
            mid = (l + r) / 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                l = mid
            else:
                r = mid
        return l*l == num or r*r == num
