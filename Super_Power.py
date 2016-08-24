class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        m = 1337
        a %= m
        # [Euler's totient theorem]
        #   a^phi(m) = 1 mod m
        # We can calculate phi(a) offline.
        # 1377 = 7 * 191
        # phi(1377) = phi(7) * phi(191)
        #           = 6 * 190
        #           = 1140
        phi = 1140 
        if not b:
            return 1
        e = 0
        for d in b:
            e = (e*10 + d) % phi
        return pow(a, e, m)