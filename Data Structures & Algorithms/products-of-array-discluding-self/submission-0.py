class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # no division, space O(n), time O(1) bc output array doesn't count for space
        
        # initialize output array with 1's
        output = [1]*len(nums)

        # add prefix for each item to output array
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i] 

        # multiply prefix of each item by its suffix product
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output