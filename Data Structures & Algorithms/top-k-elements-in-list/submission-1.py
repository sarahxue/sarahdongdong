class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort, O(n) time
        # frequency of each value
        count = {}
        # index: frequency of element, value: list of values with that frequency
        freq = [[] for i in range(len(nums)+1)]

        # count occurance of each value in nums
        for n in nums: 
            count[n] = 1 + count.get(n,0)
        # go through each value counted, at index count append value n
        for n, c in count.items():
            freq[c].append(n) #n occurs c times

        res = []
        # go through frequencies in desc order
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

