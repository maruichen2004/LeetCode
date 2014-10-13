class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        low, high = 0, x/2 + 1
        while low <= high:
            mid = (low + high) / 2
            if x < mid * mid: high = mid - 1
            else: low = mid + 1
        return int(high)
