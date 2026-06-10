class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #one pass solution 
        #time: O(n) space: O(n)
        passed = {}

        for i in range(len(nums)):
            if nums[i] in passed:
                return [passed[nums[i]],i]
            need = target - nums[i]
            passed[need] = i