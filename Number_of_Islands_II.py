class UnionFind:
    def __init__(self, n):
        self.idx = [-1] * n
        self.rank = [0] * n
        self.unions = 0
        
    def find(self, p):
        while p != self.idx[p]:
            self.idx[p] = self.idx[self.idx[p]]
            p = self.idx[p]
        return p
        
    def union(self, p, q):
        i, j = self.find(p), self.find(q)
        if i == j:
            return
        if self.rank[i] < self.rank[j]:
            self.idx[i] = j
            self.rank[j] += self.rank[i]
        else:
            self.idx[j] = i
            self.rank[i] += self.rank[j]
        self.unions += 1

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        grid, uf, res = [[[0] * n] * m], UnionFind(m*n), []
        for i, (x, y) in enumerate(positions):
            uf.idx[x*n+y] = x*n+y
            for u, v in [(x+1, y), (x-1, y), (x, y-1), (x,y+1)]:
                if 0<= u < m and 0 <= v < n and uf.idx[u*n+v] != -1:
                    uf.union(x*n+y, u*n+v)
            res.append(i+1 - uf.unions)
        return res