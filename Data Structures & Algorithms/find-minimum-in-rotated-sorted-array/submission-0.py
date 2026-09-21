class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1       # cliff is right of mid
            else:
                hi = mid   # mid could be the min, keep it
        return nums[lo]