class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key = lambda x: x[0])
        res.append(intervals[0])

        for interval in intervals[1:]:
            lastIndex = res[-1][1]
            if interval[0] <= lastIndex:
                res[-1][1] = max(lastIndex, interval[1])
            else:
                res.append(interval)
        return res
