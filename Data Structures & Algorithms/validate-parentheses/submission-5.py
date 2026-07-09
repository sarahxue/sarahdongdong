class Solution:
    def isValid(self, s: str) -> bool:
        # use stack for matching 
        # time O(n) space O(n)
        stacl = []
        hashMap = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        for b in s:
            # if is a closing bracket
            if b in hashMap:
                if len(stacl) != 0 and stacl[-1] == hashMap[b]:
                    stacl.pop()
                else:
                    return False
            else:
                stacl.append(b)
        return len(stacl) == 0
