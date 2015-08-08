class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        k, l = -1, 0
        for i in range(len(num) - 1):
            if num[i] < num[i + 1]: k = i
        if k == -1:
            num.reverse()
            return
        for i in range(len(num)):
            if num[i] > num[k]: l = i
        num[l], num[k] = num[k], num[l]
        num[k+1:] = num[:k:-1]
