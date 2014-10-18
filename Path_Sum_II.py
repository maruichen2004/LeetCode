# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        res = []
        self.pathSumRec(res, [], root, sum)
        return res
        
    def pathSumRec(self, res, cur, root, sum):
        if root is None: return
        if root.left is None and root.right is None:
            if root.val == sum: res.append(cur + [root.val])
        else:
            self.pathSumRec(res, cur + [root.val], root.left, sum - root.val)
            self.pathSumRec(res, cur + [root.val], root.right, sum - root.val)
            
