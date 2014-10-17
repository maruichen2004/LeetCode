class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if len(matrix) == 0: return 0
        area, a = 0, [0 for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                a[j] = a[j] + 1 if matrix[i][j] == "1" else 0
            area = max(area, self.largestRectangle(a))
        return area
        
    def largestRectangle(self, height):
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
