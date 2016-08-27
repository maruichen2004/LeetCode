class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        map = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}
        for i in range(len(num)/2 + 1):
            if num[i] not in map or map[num[i]] != num[-(i+1)]:
                return False
        return True