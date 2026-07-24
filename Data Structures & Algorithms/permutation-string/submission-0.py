class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # time O(n) space O(1)

        if len(s1) > len(s2):
            return False

        s1c, s2c = [0]*26, [0]*26
        for i in range(len(s1)):
            s1c[ord(s1[i]) - ord('a')] += 1
            s2c[ord(s2[i]) - ord('a')] += 1

        matches = 0
        # get starting matches from whole arrays
        for i in range(26):
            matches += (1 if s1c[i] == s2c[i] else 0)

        l = 0
        # start from index where we stopped 
        for r in range(len(s1), len(s2)):
            if matches == 26: 
                return True
            # add new letter to s2 count
            index = ord(s2[r]) - ord('a')
            s2c[index] += 1
            if s1c[index] == s2c[index]:
                matches += 1
            elif s1c[index] + 1 == s2c[index]:
                matches -= 1

            # take away letter that was cut out of window
            index = ord(s2[l]) - ord('a')
            s2c[index] -= 1
            if s1c[index] == s2c[index]:
                matches += 1
            elif s1c[index] - 1 == s2c[index]:
                matches -= 1
            l += 1
        return matches == 26