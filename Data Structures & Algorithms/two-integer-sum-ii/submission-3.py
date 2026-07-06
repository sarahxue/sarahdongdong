class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # brute force, check every pair
        # time O(n^2) space O(1)
        for i in range(len(numbers)):
            need = target - numbers[i]
            for n in range(len(numbers)-i):
                if numbers[n+i] == need:
                    return[i+1,n+i+1]
        return []