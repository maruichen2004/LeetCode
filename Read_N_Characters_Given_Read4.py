# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        res = 0
        while n > 0:
            buf4 = [""] * 4
            cur = read4(buf4)
            if cur == 0:
                return res
            for i in range(min(cur, n)):
                buf[res] = buf4[i]
                res += 1
                n -= 1
        return res