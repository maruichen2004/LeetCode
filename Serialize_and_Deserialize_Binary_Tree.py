# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        vals = []
        self._serialize(root, vals)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = iter(data.split())
        return self._deserialize(vals)
        
    def _serialize(self, root, vals):
        if root is None:
            vals.append('#')
        else:
            vals.append(str(root.val))
            self._serialize(root.left, vals)
            self._serialize(root.right, vals)
            
    def _deserialize(self, vals):
        val = next(vals)
        if val == '#':
            return None
        root = TreeNode(int(val))
        root.left = self._deserialize(vals)
        root.right = self._deserialize(vals)
        return root
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))