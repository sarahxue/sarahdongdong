class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #brute force sorting solution -> solves in space O(nlogn), time O(n) bc only sort same length
        #check for same length first (O(1))
        if len(s) != len(t):
            return False 
        sorteds = sorted(s)
        sortedt = sorted(t)
        #check if s equals t
        return sorteds == sortedt