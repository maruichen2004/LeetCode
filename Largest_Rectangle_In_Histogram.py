class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        res, stack = 0, []
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                rect = heights[stack.pop()] * (i if not stack else i-1 - stack[-1])
                res = max(res, rect)
            stack.append(i)
        return res