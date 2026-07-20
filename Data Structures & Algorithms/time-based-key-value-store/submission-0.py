class TimeMap:
    # time set O(1), get O(logn)
    # space O(m*n) # values of key * total # of keys
    def __init__(self):
        self.tmap = {} # key : list [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tmap:
            self.tmap[key] = []
        self.tmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.tmap.get(key, [])
        l,r = 0, len(values)-1
        while l <= r:
            m = (l+r) // 2
            # timestamp at m is <= timestamp, search right
            if values[m][1] <= timestamp: 
                res = values[m][0]
                l = m+1
            else: 
                r = m-1
        return res