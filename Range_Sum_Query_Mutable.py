class SegTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.val = 0
        self.left = None
        self.right = None
        
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.root = self._buildSegTree(nums, 0, len(nums)-1)
    
    def _buildSegTree(self, nums, start, end):
        if start > end:
            return None
        root = SegTreeNode(start, end)
        if start == end:
            root.val = nums[start]
        else:
            mid = (start + end) / 2
            root.left = self._buildSegTree(nums, start, mid)
            root.right = self._buildSegTree(nums, mid+1, end)
            root.val = root.left.val + root.right.val
        return root

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self._update(self.root, i, val)
        
    def _update(self, root, i, val):
        if root.start == root.end:
            root.val = val
            return
        mid = (root.start + root.end) / 2
        if i <= mid:
            self._update(root.left, i, val)
        else:
            self._update(root.right, i, val)
        root.val = root.left.val + root.right.val

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._sumRange(self.root, i, j)
        
    def _sumRange(self, root, i, j):
        if root.start == i and root.end == j:
            return root.val
        mid = (root.start + root.end) / 2
        if j <= mid:
            return self._sumRange(root.left, i, j)
        elif i >= mid + 1:
            return self._sumRange(root.right, i, j)
        else:
            return self._sumRange(root.left, i, mid) + self._sumRange(root.right, mid+1, j)


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)