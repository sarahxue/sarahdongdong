class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #make set to store in 
        seen = set()
        #for loop through nums
        for num in nums:
        #if num in nums, return true
            if num in seen:
                return True
        #else add to set and continue
            seen.add(num)
        #return false
        return False