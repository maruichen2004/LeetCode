class Solution:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
        tokens = re.split('(\D)', input)
        nums = map(int, tokens[::2])
        ops = map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, tokens[1::2])
        return self.build(0, len(nums) - 1, nums, ops)
        
    def build(self, lo, hi, nums, ops):
        if lo == hi:
            return [nums[lo]]
        return [ops[i](a, b) for i in xrange(lo, hi) \
            for a in self.build(lo, i, nums, ops) for b in self.build(i + 1, hi, nums, ops)]
