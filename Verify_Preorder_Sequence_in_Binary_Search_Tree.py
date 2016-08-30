class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        low = float('-inf')
        stack = []
        for num in preorder:
            if num < low:
                return False
            while stack and stack[-1] < num:
                low = stack[-1]
                stack.pop()
            stack.append(num)
        return True