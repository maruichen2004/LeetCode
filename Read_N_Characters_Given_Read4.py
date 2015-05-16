class Solution:
    def read(self, buf, n):
        if n == 0: return 0
        sofar = 0
        buf4 = ["", "", "", ""]
        nRead = self.read4(buf4)
        while nRead != 0 and sofar < n:
            if nRead + sofar >= n:
                for i in range(n - sofar):
                    buf[sofar + i] = buf4[i]
                return n
            else:
                for i in range(nRead):
                    buf[sofar + i] = buf4[i]
                sofar += nRead
                buf4 = ["", "", "", ""]
                nRead = self.read4(buf4)
        return sofar
