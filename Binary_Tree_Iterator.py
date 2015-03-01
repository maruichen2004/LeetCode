tion for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.cur = root

    #@return: True if there has next node, or false
    def hasNext(self):
        # write your code here
        return len(self.stack) != 0 or self.cur

    #@return: return next node
    def next(self):
        #write your code here
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        parent = self.stack.pop()
        self.cur = parent.right
        return parent

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
