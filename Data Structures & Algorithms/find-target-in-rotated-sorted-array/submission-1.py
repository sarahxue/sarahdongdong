class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # one pass binary search, conditions based on rotated sorted array characteristics
        # time O(logn) space O(1)
        l = 0
        r = len(nums)-1

        while l<=r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            # m is in left sorted portion
            elif nums[m] >= nums[l]:
                if target >= nums[l] and target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            # m is in right sorted portion
            else: 
                if target > nums[m] and target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
        return -1