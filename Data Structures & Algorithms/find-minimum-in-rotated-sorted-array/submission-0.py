class Solution:
    def findMin(self, nums: List[int]) -> int:
        # time O(logn) space O(1)
        l = 0
        r = len(nums)-1
        res = nums[0]
        while l <= r:
            # array potion already sorted
            if nums[r]>nums[l]:
                res = min(res, nums[l])
                break
            m = (l+r)//2
            res = min(res, nums[m])
            # m is in left sorted portion
            if nums[m]>=nums[l]:
                l = m+1
            else:
                r = m-1
        return res