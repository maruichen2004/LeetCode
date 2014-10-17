class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        area, i, stack = 0, 0, []
        while i <= len(height):
            if len(stack) == 0 or (i < len(height) and height[i] > height[stack[-1]]):
                stack.append(i)
                i += 1
            else:
                last = stack.pop()
                if len(stack) == 0: area = max(area, height[last] * i)
                else: area = max(area, height[last] * (i - stack[-1] - 1))
        return area
