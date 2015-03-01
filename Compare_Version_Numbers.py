class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        n1 = [int(i) for i in version1.split('.')]
        n2 = [int(i) for i in version2.split('.')]
        return self.compareVersionHelper(n1, n2)
        
    def compareVersionHelper(self, n1, n2):
        if len(n1) > len(n2): return -self.compareVersionHelper(n2, n1)
        i = 0
        while i < len(n1):
            if n1[i] > n2[i]: return 1
            elif n1[i] < n2[i]: return -1
            i += 1
        while i < len(n2):
            if n2[i] != 0: return -1
            i += 1
        return 0
