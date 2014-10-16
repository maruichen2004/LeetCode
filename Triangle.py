class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if len(triangle) == 0: return 0
        cur = triangle[0]
        for i in range(1, len(triangle)):
            next = [cur[0] + triangle[i][0]]
            for j in range(1, len(cur)):
                next.append(min(cur[j], cur[j - 1]) + triangle[i][j])
            next.append(cur[-1] + triangle[i][-1])
            cur = next
        return min(cur)
