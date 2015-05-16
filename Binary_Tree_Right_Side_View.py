class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        res = []
        self.rightSideViewHelper(root, 1, res)
        return res
        
    def rightSideViewHelper(self, root, depth, res):
        if not root: return
        if depth > len(res): res.append(root.val)
        self.rightSideViewHelper(root.right, depth + 1, res)
        self.rightSideViewHelper(root.left, depth + 1, res)
