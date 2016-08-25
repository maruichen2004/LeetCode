"""
First compute the prefix sums: first[m] is the sum of the first m numbers.
Then the sum of any subarray nums[i:k] is simply first[k] - first[i].
So we just need to count those where first[k] - first[i] is in [lower,upper].

To find those pairs, I use mergesort with embedded counting. The pairs in the left half and the pairs in the right half get counted in the recursive calls. We just need to also count the pairs that use both halves.

For each left in first[lo:mid] I find all right in first[mid:hi] so that right - left lies in [lower, upper]. Because the halves are sorted, these fitting right values are a subarray first[i:j]. With increasing left we must also increase right, meaning must we leave out first[i] if it's too small and and we must include first[j] if it's small enough.

Besides the counting, I also need to actually merge the halves for the sorting. I let sorted do that, which uses Timsort and takes linear time to recognize and merge the already sorted halves.
"""
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        sums = [0]
        for num in nums:
            sums.append(sums[-1] + num)
        return self.mergeSort(sums, 0, len(sums), lower, upper)
        
    def mergeSort(self, sums, l, r, lower, upper):
        if r - l <= 1:
            return 0
        mid = (l + r) / 2
        count = self.mergeSort(sums, l, mid, lower, upper) + self.mergeSort(sums, mid, r, lower, upper)
        i, j = mid, mid
        for left in sums[l:mid]:
            while i < r and sums[i] - left < lower:
                i += 1
            while j < r and sums[j] - left <= upper:
                j += 1
            count += j - i
        sums[l:r] = sorted(sums[l:r])
        return count