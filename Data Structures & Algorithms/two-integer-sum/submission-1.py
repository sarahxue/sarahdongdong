class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #through each in nums
        for i in range(len(nums)):
            for j in range(i+1, len(nums), 1):
                if nums[i] + nums[j] == target:
                    return [i, j]
        #through each remaining in nums 
        #return if two index sum == target 
