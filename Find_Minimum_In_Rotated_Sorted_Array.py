class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        l, r = 0, len(num) - 1
        while num[l] > num[r]:
            mid = (l + r) / 2
            if num[l] <= num[mid]: l = mid + 1
            elif num[mid] < num[r]: r = mid
        return num[l]
