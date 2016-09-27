class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        sum = (C - A) * (D - B) + (H - F) * (G - E);
        if E >= C or F >= D or B >= H or A >= G:
            return sum;
        return sum - ((min(G, C) - max(A, E)) * (min(D, H) - max(B, F)));