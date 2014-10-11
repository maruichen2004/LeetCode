class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        processed = {}
        for i in range(len(num)):
            if target - num[i] in processed:
                return [processed[target - num[i]] + 1, i + 1]
            processed[num[i]] = i
