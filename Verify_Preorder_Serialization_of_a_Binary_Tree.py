class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if not preorder:
            return False
        stack = []
        nodes = preorder.split(',')
        for i in range(len(nodes)):
            cur = nodes[i]
            while cur == '#' and len(stack) and stack[-1] == cur:
                stack.pop()
                if len(stack) == 0:
                    return False
                stack.pop()
            stack.append(cur)
        return len(stack) == 1 and stack[-1] == '#'