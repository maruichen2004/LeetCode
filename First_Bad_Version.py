# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l + 1 < r:
            mid = (l + r) / 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid
        if isBadVersion(l):
            return l
        if isBadVersion(r):
            return r
        return -1
