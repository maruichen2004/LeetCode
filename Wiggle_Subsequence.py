class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # DP
        if not nums:
            return 0
        asc = [1] * len(nums)
        dec = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    asc[i] = max(asc[i], dec[j] + 1)
                elif nums[j] > nums[i]:
                    dec[i] = max(dec[i], asc[j] + 1)
        return max(asc[-1], dec[-1])

        #Greedy, O(n)
        '''
        asc, dec = 1, 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                asc = dec + 1
            elif nums[i-1] > nums[i]:
                dec = asc + 1
        return min(len(nums), max(asc, dec))
        '''