class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if len(num) == 0: return 0
        l, r = 0, len(num) - 1
        while l < r - 1:
            mid = (l + r) / 2
            if num[l] < num[r]: return num[l]
            if num[mid] < num[r]: r = mid
            elif num[mid] > num[l]: l = mid
            else: l += 1
        return min(num[l], num[r])
