# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.idx = 0
        self.cnt = 0
        self.buf4 = [''] * 4
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        for i in range(n):
            if self.idx == self.cnt:
                self.cnt = read4(self.buf4)
                self.idx = 0
                if self.cnt == 0:
                    return i
            buf[i] = self.buf4[self.idx]
            self.idx += 1
        return n