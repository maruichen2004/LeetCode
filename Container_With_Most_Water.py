class Solution:
    # @return an integer
    def maxArea(self, height):
        l, r, maxV = 0, len(height) - 1, -1
        while l < r:
            maxV = max(maxV, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]: l += 1
            else: r -= 1
        return maxV
