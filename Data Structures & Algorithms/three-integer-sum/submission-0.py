class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #use 2 pointers
        #time O(n^2) space O(1) + sorting + outputlist -> O(m) where m = # triplets
        #O(m) = O(n^2) in worst case
        nums.sort() 
        triplets = []

        for i in range(len(nums)):
            # Skip duplicates for the first number to avoid duplicate answers
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            l = i+1
            r = len(nums)-1
            for j in range(i+1, len(nums), 1):
                while l < r:
                    if nums[l] + nums[r] == target:
                        triplets.append([nums[i], nums[l], nums[r]])
                        l+=1
                        r-=1
                        # Skip duplicates for the left pointer
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                    elif nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        l += 1
        return triplets