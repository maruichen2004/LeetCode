class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        q = collections.deque()
        visited = collections.defaultdict(lambda: collections.defaultdict(bool))
        stonesSet = set(stones)
        visited[0][0] = True
        q.append((0, 0))
        while q:
            cur, k = q.popleft()
            if cur == stones[-1]:
                return True
            for step in range(k-1, k+2):
                if step > 0 and cur+step in stonesSet and not visited[cur+step][step]:
                    q.append((cur+step, step))
                    visited[cur+step][step] = True
        return False