class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        stamps = self.data[key]
        l, r  = 0, len(stamps) - 1
        while l <= r:
            mid = (l+r) // 2
            tstamp, value = stamps[mid]
            if tstamp == timestamp: return value
            elif tstamp < timestamp:
                res = value
                l = mid + 1
            else: r = mid - 1
        return res       
