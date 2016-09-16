class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        while l + 1 < r:
            mid = (l + r) / 2
            if mid * mid > x:
                r = mid
            else:
                l = mid
        if r*r <= x:
            return r
        if l*l <= x:
            return l
