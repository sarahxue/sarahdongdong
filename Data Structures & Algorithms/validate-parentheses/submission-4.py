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
                if len(stacl) != 0:
                    top = stacl.pop()
                    # if current is a closing and doesnt match top, then string not valid
                    if hashMap[b] != top:
                        return False
                else:
                    return False
            else:
                stacl.append(b)
        return len(stacl) == 0
