# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.buf4 = [""] * 4
        self.rpos = 0
        self.wpos = 0
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        for i in range(n):
            if self.rpos == self.wpos:
                self.wpos = read4(self.buf4)
                self.rpos = 0
                if self.wpos == 0:
                    return i
            buf[i] = self.buf4[self.rpos]
            self.rpos += 1
        return n