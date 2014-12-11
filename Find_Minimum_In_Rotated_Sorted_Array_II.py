class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        res = num[0]
        l, r = 0, len(num) - 2
        while l <= r:
            mid = (l + r) / 2
            if num[mid] >= res and num[mid+1] <= res and num[mid] > num[mid+1]:
                return num[mid+1]
            elif num[mid+1] >= num[mid] and num[mid] >= res:
                l = mid + 1
            else:
                r = mid - 1
        return res
