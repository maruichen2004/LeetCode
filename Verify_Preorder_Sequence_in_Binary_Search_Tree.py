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

'''
class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        low = float('-inf')
        i = -1
        for a in preorder:
            if a < low:
                return False
            while i >= 0 and a > preorder[i]:
                low = preorder[i]
                i -= 1
            i += 1
            preorder[i] = a
        return True
'''