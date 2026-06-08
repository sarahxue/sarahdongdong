class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #brute force sorting solution 
        #sort s
        sorteds = sorted(s)
        #sort t
        sortedt = sorted(t)
        #check if s equals t
        return sorteds == sortedt