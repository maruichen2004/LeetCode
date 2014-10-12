class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        res = []
        visited = [False for i in range(len(num))]
        self.permuteUniqueRec(res, [], sorted(num), visited, 0)
        return res
        
    def permuteUniqueRec(self, res, cur, num, visited, i):
        if i == len(num):
            if cur not in res: res.append(cur)
        for j in range(len(num)):
            if visited[j] == False:
                visited[j] = True
                next = cur + [num[j]]
                self.permuteUniqueRec(res, next, num, visited, i + 1)
                next = cur
                visited[j] = False
