class Solution:
    # @param num, a list of integer
    # @return an integer
    def countsort(self, num, nd):
        count = [0] * 10
        n = len(num)
        for i in range(0, n):
            count[(num[i]/nd) %10] += 1
        for i in range(1,10):
            count[i] += count[i-1]
        output = [0] * n
        for i in range(n-1, -1, -1):
            output[count[(num[i]/nd)%10 ] - 1] = num[i]
            count[(num[i]/nd) % 10] -= 1
        return output
     
    def radixsort(self, num):
        max_n = max(num)
        nd = 1
        while max_n / nd > 0:
            num = self.countsort(num, nd)
            nd = nd * 10
        return num
         
    def maximumGap(self, num):
        if len(num) < 2:
            return 0
        num = self.radixsort(num)
        res = abs(num[1] - num[0])
        for i in xrange(2,len(num)):
            res = max(res, abs(num[i] - num[i-1]))
        return res
