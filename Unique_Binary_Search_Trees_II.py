# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        return self.generateTreesRec(1, n)
        
    def generateTreesRec(self, low, high):
        res = []
        if low > high: res.append(None)
        else:
            for i in range(low, high + 1):
                left = self.generateTreesRec(low, i - 1)
                right = self.generateTreesRec(i + 1, high)
                for j in left:
                    for k in right:
                        root = TreeNode(i)
                        root.left = j
                        root.right = k
                        res.append(root)
        return res
