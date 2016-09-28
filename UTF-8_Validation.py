class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        cnt = 0
        for num in data:
            if cnt == 0:
                if num >> 5 == 0b110:
                    cnt = 1
                elif num >> 4 == 0b1110:
                    cnt = 2
                elif num >> 3 == 0b11110:
                    cnt = 3
                elif num >> 7:
                    return False
            else:
                if num >> 6 != 0b10:
                    return False
                cnt -= 1
        return cnt == 0
                