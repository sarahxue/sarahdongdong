class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # time O(nlogm) n=length of piles, m=max bananas in a pile, space O(1)
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            k = l + ((r-l)//2)
            hours = 0
            for bananas in piles:
                hours += -(bananas//-k)
            if hours <= h:
                res = k
                r = k-1
            else:
                l = k+1
        return res