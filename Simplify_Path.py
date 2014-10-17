class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        stack, tokens = [], path.lstrip("/").split("/")
        for token in tokens:
            if token == ".." and len(stack) > 0: stack.pop()
            elif token != "." and token != ".." and len(token) > 0: stack.append(token)
        return "/" + "/".join(stack)
