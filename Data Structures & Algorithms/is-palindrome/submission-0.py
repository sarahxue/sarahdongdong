class Solution:
    def isPalindrome(self, s: str) -> bool:
        # reverse string and compare to original
        # time O(n) space O(n)
        filteredStr = ""
        for c in s:
            if c.isalnum():
                filteredStr += c.lower()
        return filteredStr == filteredStr[::-1]