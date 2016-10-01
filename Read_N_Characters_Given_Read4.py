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
        idx, cnt, buf4 = 0, 0, [''] * 4
        for i in range(n):
            if idx == cnt:
                cnt = read4(buf4)
                idx = 0
                if cnt == 0:
                    return i
            buf[i] = buf4[idx]
            idx += 1
        return n