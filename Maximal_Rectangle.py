class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        res, heights = 0, [0] * (len(matrix[0]) + 1)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            res = max(res, self.largestRectangle(heights))
        return res
        
    def largestRectangle(self, heights):
        res, stack = 0, []
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                rect = heights[stack.pop()] * (i if not stack else i-1 - stack[-1])
                res = max(res, rect)
            stack.append(i)
        return res