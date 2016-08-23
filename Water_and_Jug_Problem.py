class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        '''
        assuming we have one big enough bucket and two cups with volume x and y, respectively. Now we want to perform a series of
        operation -- pouring water in and out only by those two cups with exactly amount x or y. Somehow, there will be only z water left
        in this big bucket eventually. Then the equation will be:
            z = m * x + n * y
        m means using cup-x m times. If m is positive, it means pouring in. Otherwise, it's pouring out.
        n is similar.
        We can always find a and b to satisfy ax + bx = d where d = gcd(x, y)
        So, everything is clear, if z % d == 0, then we have (a*z/d)*x + (b*z/d)*y = z, which means m and n exist.
        '''
        return z == 0 or (z <= x + y and z % self.gcd(x, y) == 0)

    def gcd(self, x, y):
        if y == 0:
            return x
        return self.gcd(y, x%y)