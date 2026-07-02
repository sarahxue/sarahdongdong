class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "," + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        # until past end of encoded string
        while i < len(s):
            # start of individual word
            j = i
            while s[j] != ",":
                j+=1
            length = int(s[i:j]) # number of chars following ',' to read
            # add word length chars from j+1 (after separator)
            decoded_strs.append(s[j+1 : j+1+length])
            # update counter
            i = j+1+length

        return decoded_strs;