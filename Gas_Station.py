class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        tmp, total, k = 0, 0, -1
        for i in range(len(gas)):
            tmp += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if tmp < 0:
                k = i
                tmp = 0
        return k + 1 if total >= 0 else -1
