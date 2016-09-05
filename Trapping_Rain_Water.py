class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0
        res, l, r = 0, 0, len(height) - 1
        while l < r:
            min_height = min(height[l], height[r])
            if min_height == height[l]:
                l += 1
                while l < r and height[l] < min_height:
                    res += min_height - height[l]
                    l += 1
            else:
                r -= 1
                while l < r and height[r] < min_height:
                    res += min_height - height[r]
                    r -= 1
        return res