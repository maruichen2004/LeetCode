# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        res = []
        self.inorder(root, target, k, res)
        return [i[1] for i in res]
        
    def inorder(self, root, target, k, res):
        if root is not None:
            self.inorder(root.left, target, k, res)
            heapq.heappush(res, (-abs(root.val - target), root.val))
            if len(res) > k:
                heapq.heappop(res)
            self.inorder(root.right, target, k, res)
    '''
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        res, pre, suc = [], [], []
        cur = root
        while cur:
            if cur.val <= target:
                pre.append(cur)
                cur = cur.right
            else:
                suc.append(cur)
                cur = cur.left
        while k > 0:
            if len(suc) == 0 or (len(pre) > 0 and target - pre[-1].val < suc[-1].val - target):
                res.append(pre[-1].val)
                self.getPredecessor(pre)
            else:
                res.append(suc[-1].val)
                self.getSucessor(suc)
            k -= 1
        return res
        
    def getPredecessor(self, pre):
        cur = pre.pop()
        if cur.left:
            pre.append(cur.left)
            while pre[-1].right:
                pre.append(pre[-1].right)
                
    def getSucessor(self, suc):
        cur = suc.pop()
        if cur.right:
            suc.append(cur.right)
            while suc[-1].left:
                suc.append(suc[-1].left)