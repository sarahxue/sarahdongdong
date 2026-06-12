class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        #get frequency of each number 
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        #sort hashmap by value
        # sort based on highest value, index 1 of the tuple
        # reverse = true -> highest at front 
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # Output k top ones from sorted
        result = []
        for i in range(k):
            # Append the key (the actual number), which is at index 0
            result.append(sorted_freq[i][0])
            
        return result