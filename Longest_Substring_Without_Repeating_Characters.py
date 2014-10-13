class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        maxlen, substr, rear = 0, "", 0
        for front in range(len(s)):
            if s[front] not in substr: substr += s[front]
            else:
                maxlen = max(maxlen, len(substr))
                while s[rear] != s[front]: rear += 1
                rear += 1
                substr = s[rear:front + 1]
        maxlen = max(maxlen, len(substr))
        return maxlen
